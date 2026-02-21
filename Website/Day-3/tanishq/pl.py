import os
import pandas as pd
from lxml import html
from curl_cffi import requests
from urllib.parse import urljoin

PLATFORM = "tanishq"
MAX_RECORDS = 7000

BASE_OUTPUT = r"D:\30_day\output file"
BASE_PAGESAVE = r"D:\30_day\pagesave"

pl_output_path = os.path.join(BASE_OUTPUT, PLATFORM, "pl")
pl_pagesave_path = os.path.join(BASE_PAGESAVE, PLATFORM, "pl")

os.makedirs(pl_output_path, exist_ok=True)
os.makedirs(pl_pagesave_path, exist_ok=True)


headers = {
    "accept": "*/*",
    "x-requested-with": "XMLHttpRequest",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "referer": "https://www.tanishq.co.in/shop/jewellery?lang=en_IN"
}

print("===== PL SCRAPING START =====")

start = 0
page_size = 24
all_products = []
seen_urls = set()

while len(all_products) < MAX_RECORDS:

    pl_filename = os.path.join(pl_pagesave_path, f"pl_{start}.html")

    if os.path.exists(pl_filename):
        print(f"[PL] Reading Saved Page {start}")
        with open(pl_filename, "r", encoding="utf-8") as f:
            page_content = f.read()
    else:
        print(f"[PL] Fetching Page {start}")

        params = {
            "cgid": "tq-all-jewellery",
            "prefn1": "priceRecordMissing",
            "prefv1": "false",
            "start": str(start),
            "sz": str(page_size),
        }

        response = requests.get(
            "https://www.tanishq.co.in/on/demandware.store/Sites-Tanishq-Site/en_IN/Search-UpdateGrid",
            params=params,
            headers=headers,
            impersonate="chrome120"
        )

        if response.status_code != 200:
            print("Request Failed")
            break

        page_content = response.text

        with open(pl_filename, "w", encoding="utf-8") as f:
            f.write(page_content)

    tree = html.fromstring(page_content)

    product_cards = tree.xpath('//a[@class="tile-wrapper"]')

    if not product_cards:
        print("No more products found")
        break

    print(f"Products Found On Page: {len(product_cards)}")

    for card in product_cards:
        if len(all_products) >= MAX_RECORDS:
            break

        link = card.xpath('.//@href')
        name = card.xpath('.//h5//text()')

        link = link[0].strip() if link else ""
        name = " ".join([n.strip() for n in name if n.strip()])

        full_url = urljoin("https://www.tanishq.co.in", link)

        if full_url in seen_urls:
            continue

        seen_urls.add(full_url)

        all_products.append({
            "url": full_url,
            "title": name
        })

    print(f"Collected So Far: {len(all_products)}")

    start += page_size

print(f"Final Collected Products: {len(all_products)}")

pl_df = pd.DataFrame(all_products)
pl_df.to_excel(os.path.join(pl_output_path, "pl_products.xlsx"), index=False)

print("===== DONE =====")
