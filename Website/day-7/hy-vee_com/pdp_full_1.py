import pandas as pd
import requests
import json
import os
import time

excel_path = r"D:\30-day-scraping-challenge\Website\day-7\hy-vee_com\output\hyvee_scraped_output.xlsx"
output_json_path = r"D:\30-day-scraping-challenge\Website\day-7\hy-vee_com\output\hyvee_product_details1.json"
checkpoint_path = r"D:\30-day-scraping-challenge\Website\day-7\hy-vee_com\output\checkpoint1.json"

df = pd.read_excel(excel_path)
df.columns = df.columns.str.strip()

if "productId" not in df.columns:
    raise Exception(f"productId column not found. Available columns: {df.columns.tolist()}")

product_ids = df["productId"].dropna().astype(int).unique().tolist()

if os.path.exists(output_json_path):
    with open(output_json_path, "r", encoding="utf-8") as f:
        results = json.load(f)
else:
    results = []

if os.path.exists(checkpoint_path):
    with open(checkpoint_path, "r", encoding="utf-8") as f:
        processed_ids = set(json.load(f))
else:
    processed_ids = set()

headers = {
    "accept": "*/*",
    "apollographql-client-name": "aisles-online-web",
    "content-type": "application/json",
    "origin": "https://www.hy-vee.com",
    "referer": "https://www.hy-vee.com/",
    "user-agent": "Mozilla/5.0",
    "x-operation-name": "getProductDetailsWithPrice",
}

total = len(product_ids)
count = len(processed_ids)

for pid in product_ids:

    if pid in processed_ids:
        continue

    json_data = {
        "operationName": "getProductDetailsWithPrice",
        "variables": {
            "locationIds": ["266a52f4-0e7a-4729-bc6f-25c6ebaca111"],
            "retailItemEnabled": True,
            "targeted": False,
            "wicEnabled": True,
            "foodHealthScoreEnabled": True,
            "pickupLocationHasLocker": False,
            "productId": pid,
            "storeId": 1759,
        },
        "query": """query getProductDetailsWithPrice($locationIds: [ID!] = [], $retailItemEnabled: Boolean = false, $productId: Int!, $storeId: Int, $pickupLocationHasLocker: Boolean!, $targeted: Boolean = false, $wicEnabled: Boolean = false, $foodHealthScoreEnabled: Boolean = false) {
          product(productId: $productId) {
            productId
            size
            item {
              itemId
              description
              ecommerceStatus
              source
              ecommerceDefaultPrice
              images { url }
              retailItems(locationIds: $locationIds) @include(if: $retailItemEnabled) {
                retailItemId
                basePrice
                tagPrice
              }
            }
          }
          storeProducts(where: {productId: $productId, storeId: $storeId, isActive: true}) {
            storeProducts {
              storeProductId
              productId
              storeId
              onSale
              price
              basePrice
              subcategoryId
              variations {
                variationId
                description
                price
                basePrice
              }
              category {
                categoryId
                name
              }
            }
          }
        }"""
    }

    try:
        response = requests.post(
            "https://www.hy-vee.com/aisles-online/api/graphql/two-legged/getProductDetailsWithPrice",
            headers=headers,
            json=json_data,
            timeout=30
        )

        if response.status_code != 200:
            continue

        data = response.json().get("data", {})
        product_data = data.get("product", {})
        store_products_block = data.get("storeProducts", {})
        store_products_list = store_products_block.get("storeProducts", [])

        if not product_data:
            continue

        item = product_data.get("item", {})
        store_info = store_products_list[0] if store_products_list else {}
        variations_list = store_info.get("variations", [])

        result = {
            "url": f"https://www.hy-vee.com/aisles-online/p/{pid}",
            "productId": product_data.get("productId"),
            "size": product_data.get("size"),
            "description": item.get("description"),
            "ecommerceStatus": item.get("ecommerceStatus"),
            "source": item.get("source"),
            "defaultPrice": item.get("ecommerceDefaultPrice"),
            "storeProductId": store_info.get("storeProductId"),
            "price": store_info.get("price"),
            "basePrice": store_info.get("basePrice"),
            "onSale": store_info.get("onSale"),
            "subcategoryId": store_info.get("subcategoryId"),
            "categoryId": store_info.get("category", {}).get("categoryId") if store_info.get("category") else None,
            "categoryName": store_info.get("category", {}).get("name") if store_info.get("category") else None,
            "variations": variations_list
        }

        results.append(result)
        processed_ids.add(pid)
        count += 1

        with open(output_json_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)

        with open(checkpoint_path, "w", encoding="utf-8") as f:
            json.dump(list(processed_ids), f)

        print(f"Processed {count}/{total} | ProductId: {pid}")

        time.sleep(0.5)

    except Exception:
        continue