import os
import time
import pandas as pd
from curl_cffi import requests
from lxml import html

input_excel = r"D:\30-day-scraping-challenge\output file\apollotyres\pl2\apollotyres2.xlsx"

output_folder = r"D:\30-day-scraping-challenge\output file\apollotyres\detail"
pages_folder = r"D:\30-day-scraping-challenge\pagesave\apollotyres\detail"

os.makedirs(output_folder, exist_ok=True)
os.makedirs(pages_folder, exist_ok=True)

output_excel = os.path.join(output_folder, "apollotyres_detail_output.xlsx")

df = pd.read_excel(input_excel)

if "product_url" not in df.columns:
    exit()

urls = df["product_url"].dropna().str.strip().tolist()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

all_data = []

for index, url in enumerate(urls, start=1):

    page_filename = f"page_{index}.html"
    page_path = os.path.join(pages_folder, page_filename)

    try:
        if os.path.exists(page_path):
            with open(page_path, "r", encoding="utf-8") as f:
                page_content = f.read()
        else:
            response = requests.get(url, headers=headers, timeout=30)
            if response.status_code != 200:
                continue
            page_content = response.text
            with open(page_path, "w", encoding="utf-8") as f:
                f.write(page_content)
            time.sleep(2)

        tree = html.fromstring(page_content)

        name = tree.xpath('//h2[@id="itemPropertyName"]/text()')
        name = name[0].strip() if name else ""

        size = tree.xpath('//span[@id="itemPropertyTyreSize"]/text()')
        size = size[0].strip() if size else ""

        desc = tree.xpath('//div[@class="short-description"]//text()')
        desc = " ".join([i.strip() for i in desc if i.strip()])

        price = tree.xpath('//div[@class="product-price"]/span//text()')
        price = price[0].strip() if price else ""

        models = tree.xpath('//div[@class="ps_fitmodelbox"]//ul//li//text()')
        models = ", ".join([i.strip() for i in models if i.strip()])

        features = tree.xpath('//div[@class="ps_fandbbox"]//ul//li//text()')
        features = ", ".join([i.strip() for i in features if i.strip()])

        all_data.append({
            "product_url": url,
            "name": name,
            "size": size,
            "price": price,
            "description": desc,
            "compatible_models": models,
            "features_benefits": features,
            "page_saved_as": page_filename
        })

    except:
        continue

final_df = pd.DataFrame(all_data)
final_df.to_excel(output_excel, index=False)
