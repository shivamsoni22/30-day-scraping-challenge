# import os
# from lxml import html
#
# import pandas as pd
# from curl_cffi import requests
# Type = "pl2"
#
# output_base = r"D:\30-day-scraping-challenge\output file\apollotyres"
# pages_base = r"D:\30-day-scraping-challenge\pagesave\apollotyres"
#
# os.makedirs(output_base, exist_ok=True)
# os.makedirs(pages_base, exist_ok=True)
#
# output_folder = os.path.join(output_base, Type)
# pages_folder = os.path.join(pages_base, Type)
#
# os.makedirs(output_folder, exist_ok=True)
# os.makedirs(pages_folder, exist_ok=True)
#
# print("Output Folder:", output_folder)
# print("Page Save Folder:", pages_folder)
#
# input_excel_path = r"D:\30-day-scraping-challenge\output file\apollotyres\pl\apollotyres_products.xlsx"
#
# df_input = pd.read_excel(input_excel_path)
#
# if "product_url" not in df_input.columns:
#     print("product_url column not found in Excel!")
#     exit()
#
# product_urls = df_input["product_url"].dropna().tolist()
#
# print("Total URLs Found:", len(product_urls))
#
#
# cookies = {
#     '.Shop.Customer': 'ce84ce78-09df-444b-9c4f-6b519a41dcf8',
#     '.Nop.Antiforgery': 'CfDJ8MMcpDq0ziZHi9hHeknFN2kMxiliMtoM5PHEE02cTiFZFXWASt3gZd7V77orO9Y8rKeXU1zCy2XEBBeEgWfKqzb1nwDax8SxFblgKoqOsiBtlxSWUItZzKLUKLXoQPeQAOjVSpPJmA9xORc2Q7C5X5g',
#     '.Nop.Session': 'CfDJ8MMcpDq0ziZHi9hHeknFN2kZtfhFKENvVsw1VQxzfuacBMwqGP9%2F5UJWhsz7t1Yu99aDiU%2F26r3QsHJQzaMf1%2Bq0W2JZmgc4FU2mGylgNIgSPXwXQDYFtkxjdmNUu62eMpvAoA4r5cCvOlz%2BPFRVo3bcWIgG6WrZ0ezfoyXn4%2B25',
#     'ARRAffinity': '40265b14d19f236fcb24bd2e6ec9c71b71e6c28d481f1a5a021e0a87fd48c6d0',
#     'ARRAffinitySameSite': '40265b14d19f236fcb24bd2e6ec9c71b71e6c28d481f1a5a021e0a87fd48c6d0',
#     '_gcl_gs': '2.1.k1$i1771396816$u102518595',
#     '_ga': 'GA1.1.770746503.1771396818',
#     '_fbp': 'fb.1.1771396818280.910229551325260660',
#     '_gcl_aw': 'GCL.1771396946.CjwKCAiAwNDMBhBfEiwAd7ti1KNLGzfIKPAWjpZRU1XYIw7-JRkk_O5_6EpGiI14EaguF5hAJqy0-xoCq8IQAvD_BwE',
#     '_gcl_au': '1.1.997842658.1771396817.464172326.1771396974.1771396974',
#     '_ga_ZSK09WST3X': 'GS2.1.s1771396818$o1$g1$t1771401540$j56$l0$h0',
# }
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Referer': 'https://shop.apollotyres.com/hero-bike-tyres',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     # 'Cookie': '.Shop.Customer=ce84ce78-09df-444b-9c4f-6b519a41dcf8; .Nop.Antiforgery=CfDJ8MMcpDq0ziZHi9hHeknFN2kMxiliMtoM5PHEE02cTiFZFXWASt3gZd7V77orO9Y8rKeXU1zCy2XEBBeEgWfKqzb1nwDax8SxFblgKoqOsiBtlxSWUItZzKLUKLXoQPeQAOjVSpPJmA9xORc2Q7C5X5g; .Nop.Session=CfDJ8MMcpDq0ziZHi9hHeknFN2kZtfhFKENvVsw1VQxzfuacBMwqGP9%2F5UJWhsz7t1Yu99aDiU%2F26r3QsHJQzaMf1%2Bq0W2JZmgc4FU2mGylgNIgSPXwXQDYFtkxjdmNUu62eMpvAoA4r5cCvOlz%2BPFRVo3bcWIgG6WrZ0ezfoyXn4%2B25; ARRAffinity=40265b14d19f236fcb24bd2e6ec9c71b71e6c28d481f1a5a021e0a87fd48c6d0; ARRAffinitySameSite=40265b14d19f236fcb24bd2e6ec9c71b71e6c28d481f1a5a021e0a87fd48c6d0; _gcl_gs=2.1.k1$i1771396816$u102518595; _ga=GA1.1.770746503.1771396818; _fbp=fb.1.1771396818280.910229551325260660; _gcl_aw=GCL.1771396946.CjwKCAiAwNDMBhBfEiwAd7ti1KNLGzfIKPAWjpZRU1XYIw7-JRkk_O5_6EpGiI14EaguF5hAJqy0-xoCq8IQAvD_BwE; _gcl_au=1.1.997842658.1771396817.464172326.1771396974.1771396974; _ga_ZSK09WST3X=GS2.1.s1771396818$o1$g1$t1771401540$j56$l0$h0',
# }
#
# response = requests.get('https://shop.apollotyres.com/hero-hf-deluxe-kick-spoke-tyres',
#                         # cookies=cookies,
#                         headers=headers,
#                         impersonate="chrome120")
#
#
#
#
# if response.status_code != 200:
#     exit()
#
# page_path = os.path.join(pages_folder, "page_1.html")
# with open(page_path, "w", encoding="utf-8") as f:
#     f.write(response.text)
#
# tree = html.fromstring(response.text)
#
# titles = [i.strip() for i in tree.xpath('//a[@id="ps_modelTitle"]/text()') if i.strip()]
# links = tree.xpath('//a[@id="ps_modelTitle"]/@href')
#
# links = ["https://shop.apollotyres.com" + i if i.startswith("/") else i for i in links]
#
# data = []
# for t, l in zip(titles, links):
#     data.append({"product_title": t, "product_url": l})
#
# df = pd.DataFrame(data)
#
# excel_path = os.path.join(output_folder, "p2.xlsx")
# df.to_excel(excel_path, index=False)
#
# print("Done")
# print("Total:", len(df))


import os
from lxml import html
import pandas as pd
from curl_cffi import requests
import time

Type = "pl2"

output_base = r"D:\30-day-scraping-challenge\output file\apollotyres"
pages_base = r"D:\30-day-scraping-challenge\pagesave\apollotyres"

os.makedirs(output_base, exist_ok=True)
os.makedirs(pages_base, exist_ok=True)

output_folder = os.path.join(output_base, Type)
pages_folder = os.path.join(pages_base, Type)

os.makedirs(output_folder, exist_ok=True)
os.makedirs(pages_folder, exist_ok=True)

print("Output Folder:", output_folder)
print("Page Save Folder:", pages_folder)

# ===============================
# READ INPUT EXCEL
# ===============================

input_excel_path = r"D:\30-day-scraping-challenge\output file\apollotyres\pl\apollotyres_products.xlsx"

df_input = pd.read_excel(input_excel_path)

if "product_url" not in df_input.columns:
    print("product_url column not found in Excel!")
    exit()

product_urls = df_input["product_url"].dropna().str.strip().tolist()

print("Total URLs Found:", len(product_urls))

# ===============================
# HEADERS
# ===============================

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

# ===============================
# SCRAPING LOOP
# ===============================

all_data = []

for index, url in enumerate(product_urls, start=1):

    print(f"\nScraping {index} / {len(product_urls)}")
    print("URL:", url)

    try:
        response = requests.get(
            url,
            headers=headers,
            impersonate="chrome120",
            timeout=30
        )

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            continue

        # Save HTML
        page_path = os.path.join(pages_folder, f"page_{index}.html")
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(response.text)

        tree = html.fromstring(response.text)

        # Extract Listing Records
        titles = [i.strip() for i in tree.xpath('//a[@id="ps_modelTitle"]/text()') if i.strip()]
        links = tree.xpath('//a[@id="ps_modelTitle"]/@href')

        links = [
            "https://shop.apollotyres.com" + i if i.startswith("/") else i
            for i in links
        ]

        print("Records Found on this page:", len(titles))

        for t, l in zip(titles, links):
            all_data.append({
                "source_page": url,
                "product_title": t,
                "product_url": l
            })

        time.sleep(2)

    except Exception as e:
        print("Error:", e)
        continue

# ===============================
# SAVE FINAL EXCEL
# ===============================

final_df = pd.DataFrame(all_data)

excel_path = os.path.join(output_folder, "apollotyres2.xlsx")
final_df.to_excel(excel_path, index=False)

print("\nScraping Completed")
print("Total Records Collected:", len(final_df))
