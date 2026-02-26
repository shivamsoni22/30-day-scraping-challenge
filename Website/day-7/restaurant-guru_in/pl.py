import pandas as pd
from curl_cffi import requests
from lxml import html
import os
cookies = {
    'country': '9',
    'rg_check': '1',
    '_gcl_au': '1.1.854839918.1772087054',
    '_ga': 'GA1.2.1590108582.1772087054',
    '_gid': 'GA1.2.2126996532.1772087054',
    'askedloc': '1',
    'client_time_hour': '2026-02-26%2011:55:38',
    'closebnr': '1',
    'FCCDCF': '%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22df1b88f0-286d-4617-89ff-6e0e75c2a7ae%5C%22%2C%5B1772087055%2C2000000%5D%5D%22%5D%5D%5D',
    '_gat': '1',
    '_ga_N0PX6VDPSG': 'GS2.2.s1772087055$o1$g1$t1772087139$j60$l0$h0',
    'g_state': '{"i_l":0,"i_ll":1772087139942,"i_b":"pVrpGnncQpFiVDFqGc3go1kI7lx/HiZEWO5utmU5W5o","i_e":{"enable_itp_optimization":0}}',
    'FCNEC': '%5B%5B%22AKsRol-WIDQdbX0K9LJjfyr-xwCr1y9Z8NxYvqf-a3AWIB_EoZPFYQAuvqYDO_JmuSoZ-J4QnGdst4l5qZrsJa89MppGa5dENWJM5fdP2JZEFlhzYV4fKSF7DD4kCpvd-Aqh-5sIGfT8amMDf-oyurqDE5xYaLh8FA%3D%3D%22%5D%5D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'if-modified-since': 'Wed, 25 Feb 2026 18:01:27 GMT',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'cookie': 'country=9; rg_check=1; _gcl_au=1.1.854839918.1772087054; _ga=GA1.2.1590108582.1772087054; _gid=GA1.2.2126996532.1772087054; askedloc=1; client_time_hour=2026-02-26%2011:55:38; closebnr=1; FCCDCF=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5B32%2C%22%5B%5C%22df1b88f0-286d-4617-89ff-6e0e75c2a7ae%5C%22%2C%5B1772087055%2C2000000%5D%5D%22%5D%5D%5D; _gat=1; _ga_N0PX6VDPSG=GS2.2.s1772087055$o1$g1$t1772087139$j60$l0$h0; g_state={"i_l":0,"i_ll":1772087139942,"i_b":"pVrpGnncQpFiVDFqGc3go1kI7lx/HiZEWO5utmU5W5o","i_e":{"enable_itp_optimization":0}}; FCNEC=%5B%5B%22AKsRol-WIDQdbX0K9LJjfyr-xwCr1y9Z8NxYvqf-a3AWIB_EoZPFYQAuvqYDO_JmuSoZ-J4QnGdst4l5qZrsJa89MppGa5dENWJM5fdP2JZEFlhzYV4fKSF7DD4kCpvd-Aqh-5sIGfT8amMDf-oyurqDE5xYaLh8FA%3D%3D%22%5D%5D',
}

response = requests.get('https://restaurant-guru.in/Ahmedabad',
                        # cookies=cookies,
                        headers=headers,
                        impersonate ='chrome120'
                        )
print("Status Code:", response.status_code)

if response.status_code != 200:
    print("Blocked by Cloudflare")
    exit()

pagesave_dir = r"D:\30-day-scraping-challenge\pagesave"
os.makedirs(pagesave_dir, exist_ok=True)

page_file_path = os.path.join(pagesave_dir, "Ahmedabad_page1.html")

with open(page_file_path, "wb") as f:
    f.write(response.content)

print("Page HTML saved successfully")


tree = html.fromstring(response.content)


# //a[@class="notranslate link link--secondary card__link link-span "]/@href
# //a[@class="notranslate link link--secondary card__link link-span "]//text()
# print(response.text)
# print(response.status_code)


names = tree.xpath('//div[@class="rest-card__title "]/a/h3/text()')
url = tree.xpath('//div[@class="rest-card__title "]/a/@href')

print("Names Found:", len(names))
print("url Found:", len(url))


records = []

for name,  link in zip(names, url):
    records.append({
        "Hotel Name": name.strip(),
        "Hotel URL":  link if link.startswith("/") else link
    })

df = pd.DataFrame(records)
output_dir = r"D:\30-day-scraping-challenge\output file\restaurant-guru"
os.makedirs(output_dir, exist_ok=True)

file_path = os.path.join(output_dir, "restaurant-guru.xlsx")
df.to_excel(file_path, index=False)

print("Excel file saved successfully")