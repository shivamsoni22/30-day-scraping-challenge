from curl_cffi import requests
from lxml import html
import pandas as pd
import os

base_url = "https://shop.apollotyres.com/custom-category-search"
Type = "pl"

output_base = r"D:\30-day-scraping-challenge\output file\apollotyres"
pages_base = r"D:\30-day-scraping-challenge\pagesave\apollotyres"

# ==========================
# CREATE MAIN FOLDERS
# ==========================
os.makedirs(output_base, exist_ok=True)
os.makedirs(pages_base, exist_ok=True)

# ==========================
# CREATE WEBSITE SUBFOLDERS
# ==========================
output_folder = os.path.join(output_base, Type)
pages_folder = os.path.join(pages_base, Type)

os.makedirs(output_folder, exist_ok=True)
os.makedirs(pages_folder, exist_ok=True)

print("Output Folder:", output_folder)
print("Page Save Folder:", pages_folder)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

params = {"q": "hero"}

response = requests.get(
    base_url,
    params=params,
    headers=headers,
    impersonate="chrome120"
)

if response.status_code != 200:
    exit()

page_path = os.path.join(pages_folder, "page_1.html")
with open(page_path, "w", encoding="utf-8") as f:
    f.write(response.text)

tree = html.fromstring(response.text)

titles = [i.strip() for i in tree.xpath('//h2[@class="product-titlecar"]/a//text()') if i.strip()]
links = tree.xpath('//div[@class="buttons"]/a/@href')

links = ["https://shop.apollotyres.com" + i if i.startswith("/") else i for i in links]

data = []
for t, l in zip(titles, links):
    data.append({"product_title": t, "product_url": l})

df = pd.DataFrame(data)

excel_path = os.path.join(output_folder, "apollotyres_products.xlsx")
df.to_excel(excel_path, index=False)

print("Done")
print("Total:", len(df))
