import os
import pandas as pd
from lxml import html
from curl_cffi import requests

PLATFORM = "tanishq"
LIMIT = 100

BASE_PATH = r"D:\30-day-scraping-challenge"
INPUT_FILE = os.path.join(BASE_PATH, "output file", PLATFORM, "pl", "pl_products.xlsx")
PDP_OUTPUT_PATH = os.path.join(BASE_PATH, "output file", PLATFORM, "pdp")
PDP_PAGESAVE_PATH = os.path.join(BASE_PATH, "pagesave", PLATFORM, "pdp")

os.makedirs(PDP_OUTPUT_PATH, exist_ok=True)
os.makedirs(PDP_PAGESAVE_PATH, exist_ok=True)
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'cookie': 'dwac_7a7354651d443450efb4c08f5d=wtnyv5dqtuB68UohrISW5TBTkWwRr66uWAY%3D|dw-only|||INR|false|Asia%2FCalcutta|true; cqcid=bcnAuNnaAPvwrjgy9xEeq90sHl; cquid=||; sid=wtnyv5dqtuB68UohrISW5TBTkWwRr66uWAY; dwanonymous_24bf461558a7367089d150cfca7d7c9b=bcnAuNnaAPvwrjgy9xEeq90sHl; __cq_dnt=0; dw_dnt=0; dwsid=Ln8h2OxAtmDlSLcFNPLkEtz1Qgtqha4ux7_jyYLMMqYZ_HUqTWZU5hFj9OR6OQxzI0XGaFacM3iMzZivtWK_ng==; _cfuvid=CvDK7zMw3uYQ5DZcYtwG0BlU7LRwXC6PGYcL5ihm7Rc-1771568533954-0.0.1.1-604800000; _sfid_d199={%22anonymousId%22:%22d5565a963700d793%22%2C%22consents%22:[{%22consent%22:{%22purpose%22:%22Tracking%22%2C%22provider%22:%22Example%20Consent%20Manager%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222026-02-20T06:22:16.124Z%22%2C%22lastSentTime%22:%222026-02-20T06:22:16.127Z%22}]}; _evga_3c13={%22uuid%22:%2219d08984dc94afb1%22}; _sfid_ef75={%22anonymousId%22:%2219d08984dc94afb1%22%2C%22consents%22:[]}; jarvis-id=7aea5c01-9be5-4f33-8b24-bc1d4f98383b; _gcl_au=1.1.930795718.1771568538; fw_uid={%22value%22:%22d46dcaca-2b92-4303-baf9-b92686b4edba%22%2C%22createTime%22:%222026-02-20T06:22:18.775Z%22}; _gid=GA1.3.179410516.1771568540; FPID=FPID2.3.IDtxZ2P%2FsVGdnQmLiOGAbtRafzF042nvXng%2B0Gru%2BiY%3D.1771568540; FPLC=kKUpvUErzKuxY33KTtX3FKMFJKqLREACTbbBg5OglRjavq2fTm9V5Aj3S8PVia%2Fc59OMeHVIKp73kyD384IasZ2G9LKn19a1FV9%2B4WBCScQDyVglyf9bXKHW43TG8g%3D%3D; FPAU=1.1.930795718.1771568538; _fbp=fb.2.1771568545130.744847161191153229; allowedCookie=yes; __cq_uuid=bcnAuNnaAPvwrjgy9xEeq90sHl; fw_bid={%22value%22:%225a8mav%22%2C%22createTime%22:%222026-02-20T06:22:29.875Z%22}; fw_chid={%22value%22:%223XWLXm6%22%2C%22createTime%22:%222026-02-20T06:22:30.415Z%22}; dwpersonalization_24bf461558a7367089d150cfca7d7c9b=5f1ca1730dd103bcf8f1e2e74620260519183000000; th_external_id=34294a2c7e02d86afca9c0866941dc5917cdfc2991baa2b79c7774bfa3f217f8; tangiblee:widget:user=9af3bab2-2f75-4260-b4a2-5f357f172b29; yotpo_pixel=6c7d20fa-fec4-4a3e-9899-6dadb24228a5; _sp_ses.e677=*; fw_se={%22value%22:%22fws2.2680c268-7d97-4f01-921c-72b4dd14ddc1.2.1771570780244%22%2C%22createTime%22:%222026-02-20T06:59:40.246Z%22}; __cq_seg=0~0.11!1~0.20!2~0.28!3~0.32!4~-0.63!5~0.16!6~-0.37!7~-0.21!8~0.39!9~-0.03!f0~15~5; _dc_gtm_UA-62831342-10=1; __cf_bm=Uqh0Itre8G4ReQg.DMRh1BMul9Qvj5Pb4Pp_w7Z.7E4-1771571918-1.0.1.1-06D4dVaW0gXmYr9LFhlhsmDfGmLRq0d2k25QmQVV1nxlnCZbap3nv_5L8ERzC00AJMzh8A9tlxEfJZvXO39esmraj8fnZqbjNBhDhHblZ2I; cf_clearance=o3hiQl2YTyhe04DqDzgZmOysGUsl7qALjkviISL27II-1771571920-1.2.1.1-tcZZluFENOeBh0clb3MeyuLJMPpi.4OSuum3yTMTnOYbM.D73TP5JAMzJkVDsgpRZtL8w.lD3SicBbiMd_lsQhGC8odCrzP0hIZRRrzKatSErGetYtk8ji2BhJXTvnAvOHx2De0USdWvl7lIQgA4.5v5cvK12qJSNjyn9GxiZPKsHtJAuzvmvJAKMsTuhIOH_vJTceiQndn5eOG.mpGO6ytwyi7tZRSFHMEgxRPqQ7A; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22N%2FA%22%2C%22expiryDate%22%3A%222027-02-20T07%3A18%3A41.498Z%22%7D; __rtbh.aid=%7B%22eventType%22%3A%22aid%22%2C%22id%22%3A%2255400304.1771568540.%22%2C%22expiryDate%22%3A%222027-02-20T07%3A18%3A41.498Z%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%223CwVr3Fr1mfrTzXxZMgX%22%2C%22expiryDate%22%3A%222027-02-20T07%3A18%3A41.499Z%22%7D; __cq_bc=%7B%22bkck-Tanishq%22%3A%5B%7B%22id%22%3A%2250d3i3sztaba09%22%2C%22sku%22%3A%2250d3i3sztaba092ja000224%22%7D%2C%7B%22id%22%3A%22501151sttaga02%22%2C%22sku%22%3A%22501151sttaga023ia011960%22%7D%2C%7B%22id%22%3A%2250d6vdfalaa09%22%2C%22sku%22%3A%2250d6vdfallaa092bd000017%22%7D%5D%7D; _ga=GA1.3.55400304.1771568540; _uetsid=863fcbf00e2411f1bad0fda0a5317d21; _uetvid=864006800e2411f1bc20477675aeac91; fs_uid=#o-1E5EGV-na1#492aeb83-a242-4cbf-a09a-edc66b9b5d79:c2cbee55-e4be-413d-91c5-bcac34d781fc:1771568544365::16#/1803104575; cto_bundle=dJ4HAl9MTGZEcXg2VzdTc2hLRXh1MnkwbEc4VlZ5Z2RvM0hWV2doYWkzbnB2JTJCM1lCaiUyQk9lZ3liN3VDaXNoMWowUDVRY21oRTlKWXNIT3U1Z09xczR1OWhGNHZrV3RCTHZXZVcxUnBqemdneEE4MGJRRnJFTyUyQnUlMkZ5V1AxQk9PQmxVcExj; _sp_id.e677=f85da4d07ccd6f5e.1771569712.1.1771571923.1771569712; _ga_DDF7077Y7T=GS2.1.s1771568540$o1$g1$t1771571923$j58$l0$h0; fs_lua=1.1771571627814; _ga_JBYD0RCS6E=GS2.1.s1771568540$o1$g1$t1771571929$j52$l0$h1997734385; _ga_LK5M8GFCJ5=GS2.1.s1771568540$o1$g1$t1771571937$j32$l0$h1295243199',
}

params = {
    'lang': 'en_IN',
}

session = requests.Session(
    params=params,
    # cookies=cookies,
    headers=headers,
    impersonate="chrome120"
    )

df = pd.read_excel(INPUT_FILE)
urls = df["url"].dropna().tolist()[:LIMIT]

pdp_data = []

for idx, url in enumerate(urls, 1):

    file_name = os.path.join(PDP_PAGESAVE_PATH, f"pdp_{idx}.html")

    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as f:
            page_content = f.read()
    else:
        response = session.get(url)
        if response.status_code != 200:
            continue
        page_content = response.text
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(page_content)

    tree = html.fromstring(page_content)

    name = tree.xpath('//meta[@property="og:title"]/@content')
    name = name[0].strip() if name else ""

    price = tree.xpath('//p[contains(@class,"saleprice")]//text()')
    price = " ".join([p.strip() for p in price if p.strip()])

    mrp = tree.xpath('//p[contains(@class,"list-price")]//text()') or "N/A"
    mrp = " ".join([m.strip() for m in mrp if m.strip()])
    mrp = mrp if mrp else "N/A"

    offer = tree.xpath('//div[contains(@class,"offer-slider-container")]//text()')
    offer = " ".join([o.strip() for o in offer if o.strip()])

    pdp_data.append({
        "url": url,
        "name": name,
        "price": price,
        "mrp": mrp,
        "offer": offer
    })

output_file = os.path.join(PDP_OUTPUT_PATH, "pdp_data.xlsx")
pd.DataFrame(pdp_data).to_excel(output_file, index=False)
