from curl_cffi import requests
from lxml import html
import pandas as pd
import os
import time
from datetime import datetime

# ========================
# CONFIG
# ========================

PLATFORM = "restaurant-guru"
CITY = "Ahmedabad"

BASE_OUTPUT = r"D:\30-day-scraping-challenge\output file"
BASE_PAGESAVE = r"D:\30-day-scraping-challenge\pagesave"

HEADERS = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'referer': f'https://restaurant-guru.in/{CITY}',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

BASE_URL = f"https://restaurant-guru.in/{CITY}" + "/{}"

# ========================
# FOLDER STRUCTURE
# ========================

pl_output_path = os.path.join(BASE_OUTPUT, PLATFORM, "pl")
pl_pagesave_path = os.path.join(BASE_PAGESAVE, PLATFORM, "pl")

os.makedirs(pl_output_path, exist_ok=True)
os.makedirs(pl_pagesave_path, exist_ok=True)

# ========================
# SCRAPING START
# ========================

page = 1
records = []

while True:
    print(f"\nScraping Page: {page}")

    url = BASE_URL.format(page)

    response = requests.get(url, headers=HEADERS)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("Stopping: Non-200 status")
        break

    try:
        data = response.json()
    except Exception as e:
        print("JSON parse failed. Possibly blocked.")
        break

    html_content = data.get("html", "")

    if not html_content:
        print("No HTML content found inside JSON. Breaking.")
        break

    # Save raw HTML extracted from JSON
    page_file_path = os.path.join(
        pl_pagesave_path,
        f"{CITY}_page{page}.html"
    )

    with open(page_file_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    tree = html.fromstring(html_content)

    # Correct XPath based on actual structure
    names = tree.xpath('//h2[@class="item__title"]/text()')
    urls = tree.xpath('//div[contains(@class,"rest-card__title")]/a/@href')

    if not names:
        print("No restaurant data found. Breaking loop.")
        break

    print(f"Found {len(names)} restaurants on page {page}")

    for name, link in zip(names, urls):

        records.append({
            "Platform": PLATFORM,
            "City": CITY,
            "Page Number": page,
            "Restaurant Name": name.strip(),
            "Restaurant URL": link,
            "Scrape Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    page += 1
    time.sleep(2)

# ========================
# SAVE EXCEL
# ========================

if records:
    df = pd.DataFrame(records)

    df.drop_duplicates(subset=["Restaurant URL"], inplace=True)

    today = datetime.now().strftime("%Y-%m-%d")
    file_name = f"{PLATFORM}_pl_{today}.xlsx"

    file_path = os.path.join(pl_output_path, file_name)
    df.to_excel(file_path, index=False)

    print("\nExcel file saved successfully")
    print("Total Restaurants:", len(df))
else:
    print("No data collected.")