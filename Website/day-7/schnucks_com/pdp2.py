import time
import pandas as pd
from curl_cffi import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'if-none-match': '"172yqd3yzdn1to4"',
    'priority': 'u=0, i',
    'referer': 'https://schnucks.com/shop/bakery/breakfast-pastries',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'cookie': 'TS01b763b5=0182a5a6cf8580c9ce248373fae9b93903246b0623905cb2bace370917a8e61b5783714167468eef1d90c5ae8f1595329a6d2965f0; _fbp=fb.1.1772113910298.734946929833270260; _gid=GA1.2.1304019095.1772113911; _pin_unauth=dWlkPU5qVXpZall5WldJdE1qVXlOUzAwTmpKaUxXSmlaV0V0TVRFek5tVTFZMkptWkRobA; __privaci_cookie_consent_uuid=b499cf06-296a-4762-a674-186f88c6f1ac:4; __privaci_cookie_consent_generated=b499cf06-296a-4762-a674-186f88c6f1ac:4; _clck=1s8etnc%5E2%5Eg3w%5E0%5E2248; _tt_enable_cookie=1; _ttp=01KJD3H0ET8739F0T2E7W44S5P_.tt.1; _gcl_au=1.1.925421708.1772113921; __privaci_cookie_consents={"consents":{"1":1,"2":1,"4":1,"5":1},"location":"GJ#IN","lang":"en","gpcInBrowserOnConsent":false,"gpcStatusInPortalOnConsent":false,"status":"record-consent-success","implicit_consent":false}; __privaci_latest_published_version=5; ajs_anonymous_id=466e4b25-d10a-4c1c-9b89-b11d70fd7eb8; _conv_v=vi%3A1*sc%3A1*cs%3A1772113911*fs%3A1772113911*pv%3A7*exp%3A%7B%7D*seg%3A%7B%7D; _conv_s=sh%3A1772113910784-0.6276341739789632*si%3A1*pv%3A7; _gat_UA-3017216-1=1; _gat_%5Bobject%20Object%5D=1; _gat_gtag_UA_3017216_1=1; _ga=GA1.1.1169088979.1772113911; _ga_VS0TEWYZ5P=GS2.1.s1772113911$o1$g1$t1772113993$j60$l0$h0; _clsk=kkpz7m%5E1772113994318%5E6%5E1%5El.clarity.ms%2Fcollect; ttcsid=1772113920489::qeTY7sgt3y6xq5uvLFfb.1.1772113994326.0; ttcsid_CD7AQCJC77U5U64QBH8G=1772113920486::fFE7EOd3xPbld7M7lQvC.1.1772113994326.1; datadome=fi2T0txUSopa0Jrb9WWq815Cj8HfDP2JlfuhAeuzf5NIV3eceBroakLseuTmb3yV6yKGWTxPRK7rtkrz_eQ3CdT6siD9Y7tBSuSQQ4V8JVpAAIHHgqI688auEPRqGu0y',
}

token = ""
proxyModeUrl = ""
proxies = {
    "http": proxyModeUrl,
    "https": proxyModeUrl,
}

results_data = []
url ='https://schnucks.com/products/1121586/schnucks-6-count-assorted-cake-donut-14-oz'

def make_request(i, max_retries=3, backoff=2):
    for attempt in range(1, max_retries + 1):
        try:
            r = requests.get(
                url,
                # params=params,
                headers=headers,
                # cookies=cookies,
                impersonate="chrome120",
                timeout=200,
                proxies=proxies,
                verify=False
       )

            credit = r.headers.get('scrape.do-request-cost', 'NA')

            if 'Schnucks - 6 Count Assorted Cake Donut (14 Oz)' in r.text and '5.99' in r.text:
                return {
                    "request_no": i,
                    "attempt": attempt,
                    "status": "GOOD",
                    "http_status": r.status_code,
                    "credit": credit
                }

            if attempt < max_retries:
                time.sleep(backoff ** attempt)
                continue

            return {
                "request_no": i,
                "attempt": attempt,
                "status": "BAD",
                "http_status": r.status_code,
                "credit": credit
            }

        except Exception as e:
            if attempt == max_retries:
                return {
                    "request_no": i,
                    "attempt": attempt,
                    "status": "ERROR",
                    "http_status": "NA",
                    "credit": "NA",
                    "error": str(e)
                }

            time.sleep(backoff ** attempt)
    return None

if __name__ == "__main__":
    num_requests = 1000
    max_workers = 100

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(make_request, i) for i in range(1, num_requests + 1)]
        for future in as_completed(futures):
            result = future.result()
            results_data.append(result)
            print(result)

    df = pd.DataFrame(results_data)
    df.to_excel("date_availability_report.xlsx", index=False)

    print("Excel file saved")