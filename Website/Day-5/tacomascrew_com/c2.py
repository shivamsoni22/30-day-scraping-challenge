from curl_cffi import requests

cookies = {
    'CurrentLanguageId': 'a26095ef-c714-e311-ba31-d43d7e4e88b2',
    'SetContextLanguageCode': 'en-us',
    'CurrentCurrencyId': '30b432b9-a104-e511-96f5-ac9e17867f77',
    'SetContextPersonaIds': 'd06988c0-9358-4dbb-aa3d-b7be5b6a7fd9',
    'XCONNECT_VISIT_ID': 'c608b36c-4832-42fd-b9d9-7848681ea44b',
    'XCONNECT_VISITOR_ID': '6688762f-550d-4ef9-8e75-fa8a7e28c39d',
    'InsiteCacheId': '334662c1-c443-4249-9342-b3a827cbb5a7',
    '_gcl_au': '1.1.1437097482.1771924752',
    '_gid': 'GA1.2.517581291.1771924754',
    'FirstPage': 'false',
    'CurrentFulfillmentMethod': 'Ship',
    'CurrentPickUpWarehouseId': '664fd364-efc6-40ad-9a1f-ab9800d1fa32',
    'RecentlyViewedProducts': '%5b%7b%22Key%22%3a%22018-631-1%22%2c%22Value%22%3a%222026-02-24T09%3a20%3a26.4498375%2b00%3a00%22%7d%5d',
    'XCONNECT_LAST_QUERY_VALUE': '868ee57b-35e2-4892-8297-ac94010af68f',
    'XCONNECT_LAST_QUERY': '21b0bae2-d43e-4ae7-8862-0baa6121d83f',
    '_dc_gtm_UA-38296018-1': '1',
    '_ga': 'GA1.2.804326206.1771924752',
    '_ga_XZLHCD4MQE': 'GS2.1.s1771928375$o2$g1$t1771928458$j58$l0$h1305832655',
    'XCONNECT_LAST_PAGE_LOAD': '%2faccount%2fisauthenticated',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'if-modified-since': 'Tue, 24 Feb 2026 10:20:04 GMT',
    'if-none-match': 'W/"f0d9cdd5cdd24f5db0d44641d1d548a0"',
    'priority': 'u=1, i',
    'referer': 'https://www.tacomascrew.com/Catalog/fasteners/bolts/cap-screws-and-hex-bolts',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'CurrentLanguageId=a26095ef-c714-e311-ba31-d43d7e4e88b2; SetContextLanguageCode=en-us; CurrentCurrencyId=30b432b9-a104-e511-96f5-ac9e17867f77; SetContextPersonaIds=d06988c0-9358-4dbb-aa3d-b7be5b6a7fd9; XCONNECT_VISIT_ID=c608b36c-4832-42fd-b9d9-7848681ea44b; XCONNECT_VISITOR_ID=6688762f-550d-4ef9-8e75-fa8a7e28c39d; InsiteCacheId=334662c1-c443-4249-9342-b3a827cbb5a7; _gcl_au=1.1.1437097482.1771924752; _gid=GA1.2.517581291.1771924754; FirstPage=false; CurrentFulfillmentMethod=Ship; CurrentPickUpWarehouseId=664fd364-efc6-40ad-9a1f-ab9800d1fa32; RecentlyViewedProducts=%5b%7b%22Key%22%3a%22018-631-1%22%2c%22Value%22%3a%222026-02-24T09%3a20%3a26.4498375%2b00%3a00%22%7d%5d; XCONNECT_LAST_QUERY_VALUE=868ee57b-35e2-4892-8297-ac94010af68f; XCONNECT_LAST_QUERY=21b0bae2-d43e-4ae7-8862-0baa6121d83f; _dc_gtm_UA-38296018-1=1; _ga=GA1.2.804326206.1771924752; _ga_XZLHCD4MQE=GS2.1.s1771928375$o2$g1$t1771928458$j58$l0$h1305832655; XCONNECT_LAST_PAGE_LOAD=%2faccount%2fisauthenticated',
}

params = {
    'path': '/Catalog/fasteners/bolts/cap-screws-and-hex-bolts',
}

response = requests.get('https://www.tacomascrew.com/api/v1/catalogpages',
                        params=params,
                        # cookies=cookies,
                        headers=headers
                        )

