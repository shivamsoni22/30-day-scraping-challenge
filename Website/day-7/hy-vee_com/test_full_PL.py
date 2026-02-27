import os
import pandas as pd
from curl_cffi import requests
cookies = {
    '_pin_unauth': 'dWlkPU5UZGxOemcwTUdFdE4ySmpNQzAwTjJGaExUbGxZVEV0TXpFMVpXSTFOREZrWkdWaQ',
    'com.silverpop.iMAWebCookie': '4de9165b-086e-7ae2-8947-2528ba29b062',
    '_gcl_au': '1.1.980378843.1772112454',
    '_ga': 'GA1.1.1275940071.1772112454',
    'hyveeSessionId': '44c79014-07a6-4d0f-b2d0-3c41cbff2d99',
    '_tt_enable_cookie': '1',
    '_ttp': '01KJD24941ZCCEPN1JM754YBPY_.tt.1',
    '_fbp': 'fb.1.1772112456070.538203930757108244',
    'rskxRunCookie': '0',
    'rCookie': 'ikf54kuof98dq5bnhahqlmm3i0fk3',
    'BIGipServer~Web_Administrators~Shared_VPC_pool': '!2aRfy4bzqCSm+xZ4QmxZpmwNFKlAz3UZt9Qp9BE5fn1Z0o+B8apo4FpH/VfYmfhJwapsOfJMWkgQ/g==',
    'store': '%257B%2522address%2522%253A%25228701%2520Douglas%2520Avenue%2522%252C%2522city%2522%253A%2522Urbandale%2522%252C%2522latitude%2522%253A41.6294%252C%2522longitude%2522%253A-93.7369%252C%2522name%2522%253A%2522Urbandale%2522%252C%2522state%2522%253A%2522Iowa%2522%252C%2522storeId%2522%253A%25221759%2522%252C%2522zip%2522%253A%252250322%2522%257D',
    '__Host-hy-vee-main-hy-vee-auth.csrf-token': 'dd6a1c5bb0b311b554dc539b2d7d5d16585a9bab5fbbcd5295486e41a43e4263%7C83410a2c520ce5e7fb10a2cc604c9eaf65c77a1baee6578c596fa06ba17b3f8a',
    '__Secure-hy-vee-main-hy-vee-auth.callback-url': 'https%3A%2F%2Fwww.hy-vee.com',
    'navigation': 'aisles',
    'kampyle_userid': '3eb0-e365-a738-4049-9154-e62f-9c28-570a',
    'kampyleUserSession': '1772172371160',
    'kampyleUserSessionsCount': '1',
    'kampyleUserPercentile': '55.139992279846325',
    'cf_clearance': 'LGr.icJOvKjDNzKFyb5uhw2SPPIDCjkC9qyvpW8nPzQ-1772185457-1.2.1.1-RyKbj7FfrzDEuobm8eiALi.TSRGMchOLioSV0ofLinhAUvDYln06GEBhNN3RYshrAxzlwZDVM1uzO6OESD4iEcJCnOPESMbbRpGrlTo57VIDxB6Pf0zvyBiqqIW8x2PZvMKMBiqkF58MdbESMMzuHlItLznIsTGEmzdx9ok0_RuXy4_gQVTYNwRJa01TuJ8ttnqcP6M5sVu652GAG1H00xb0cIg899iCjzUWEMl.ZGw',
    'com.silverpop.iMA.session': '58a07650-3b17-9c1a-e896-29baa4d887de',
    '__cf_bm': 'Qd4EZKQy5KlrZWrEGdwqdndWDdbvNpy8caFR9XRwX0w-1772185876-1.0.1.1-Gpj6l1qYR.PZhHbQAD_VJR4R7MeByO2fwNwA3QuqPpMwx2K4dcnP1dr_ntkunscDhEMWST_pxbcmKEb_K3UQK7bV3aysfKdnqR7wCru8OaQ',
    'com.silverpop.iMA.page_visit': '-1454635165:-1043156171:-1729006372:',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Feb+27+2026+15%3A21%3A23+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IN%3BGJ',
    'lastRskxRun': '1772185887326',
    'ttcsid': '1772185455271::2tedkdDwuYLhG9-53fO9.3.1772185888003.0',
    'ttcsid_C9JGOSJC77U3SHFPL600': '1772185455271::auIZejG-Dw50l6x1chl2.3.1772185888003.1',
    'kampyleSessionPageCounter': '6',
    'aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod': '{%22recordingID%22:%226-019c9e74-c03a-7010-aafd-a24035c0a46d%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772185894482%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:%2212.024883669213548%22%2C%22clearsIdentifiedUser%22:false}',
    'aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod': '{%22heartbeat%22:1772185894482}',
    '_ga_3Q3YNGZLDP': 'GS2.1.s1772184997$o3$g1$t1772185895$j43$l0$h189743630',
    'aisles-online-state': 'Fe26.2**d254e747469d72182fa6a181a34d2f6f46b4b9f5276d6b737b75dfc6c3a4aa94*Y-ni23Y4KDcjNBpIeC4KMg*EPNwh_5b8Ji3QQebbXA0fF_CqqcDYicKkWwYvNLDFp2DzGfoasjkF6V7vLnaOLE3**902eae28f3f582d471b5420075cb90bcdd2a90e8108dd7784ead8e7357a77fa0*lG06avFjTgL9IY0HSBWwqUlHUzr0GYfsqG7yZtHjP_A',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'aisles-online-web',
    'content-type': 'application/json',
    'origin': 'https://www.hy-vee.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hy-vee.com/aisles-online/search?search=milk',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-hy-vee-correlation-id': 'fd74e9fc-f855-4aa2-aa79-f2a5e51ad465',
    'x-operation-name': 'GetProductsAndFiltersFromElasticsearch',
    # 'cookie': '_pin_unauth=dWlkPU5UZGxOemcwTUdFdE4ySmpNQzAwTjJGaExUbGxZVEV0TXpFMVpXSTFOREZrWkdWaQ; com.silverpop.iMAWebCookie=4de9165b-086e-7ae2-8947-2528ba29b062; _gcl_au=1.1.980378843.1772112454; _ga=GA1.1.1275940071.1772112454; hyveeSessionId=44c79014-07a6-4d0f-b2d0-3c41cbff2d99; _tt_enable_cookie=1; _ttp=01KJD24941ZCCEPN1JM754YBPY_.tt.1; _fbp=fb.1.1772112456070.538203930757108244; rskxRunCookie=0; rCookie=ikf54kuof98dq5bnhahqlmm3i0fk3; BIGipServer~Web_Administrators~Shared_VPC_pool=!2aRfy4bzqCSm+xZ4QmxZpmwNFKlAz3UZt9Qp9BE5fn1Z0o+B8apo4FpH/VfYmfhJwapsOfJMWkgQ/g==; store=%257B%2522address%2522%253A%25228701%2520Douglas%2520Avenue%2522%252C%2522city%2522%253A%2522Urbandale%2522%252C%2522latitude%2522%253A41.6294%252C%2522longitude%2522%253A-93.7369%252C%2522name%2522%253A%2522Urbandale%2522%252C%2522state%2522%253A%2522Iowa%2522%252C%2522storeId%2522%253A%25221759%2522%252C%2522zip%2522%253A%252250322%2522%257D; __Host-hy-vee-main-hy-vee-auth.csrf-token=dd6a1c5bb0b311b554dc539b2d7d5d16585a9bab5fbbcd5295486e41a43e4263%7C83410a2c520ce5e7fb10a2cc604c9eaf65c77a1baee6578c596fa06ba17b3f8a; __Secure-hy-vee-main-hy-vee-auth.callback-url=https%3A%2F%2Fwww.hy-vee.com; navigation=aisles; kampyle_userid=3eb0-e365-a738-4049-9154-e62f-9c28-570a; kampyleUserSession=1772172371160; kampyleUserSessionsCount=1; kampyleUserPercentile=55.139992279846325; cf_clearance=LGr.icJOvKjDNzKFyb5uhw2SPPIDCjkC9qyvpW8nPzQ-1772185457-1.2.1.1-RyKbj7FfrzDEuobm8eiALi.TSRGMchOLioSV0ofLinhAUvDYln06GEBhNN3RYshrAxzlwZDVM1uzO6OESD4iEcJCnOPESMbbRpGrlTo57VIDxB6Pf0zvyBiqqIW8x2PZvMKMBiqkF58MdbESMMzuHlItLznIsTGEmzdx9ok0_RuXy4_gQVTYNwRJa01TuJ8ttnqcP6M5sVu652GAG1H00xb0cIg899iCjzUWEMl.ZGw; com.silverpop.iMA.session=58a07650-3b17-9c1a-e896-29baa4d887de; __cf_bm=Qd4EZKQy5KlrZWrEGdwqdndWDdbvNpy8caFR9XRwX0w-1772185876-1.0.1.1-Gpj6l1qYR.PZhHbQAD_VJR4R7MeByO2fwNwA3QuqPpMwx2K4dcnP1dr_ntkunscDhEMWST_pxbcmKEb_K3UQK7bV3aysfKdnqR7wCru8OaQ; com.silverpop.iMA.page_visit=-1454635165:-1043156171:-1729006372:; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+27+2026+15%3A21%3A23+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IN%3BGJ; lastRskxRun=1772185887326; ttcsid=1772185455271::2tedkdDwuYLhG9-53fO9.3.1772185888003.0; ttcsid_C9JGOSJC77U3SHFPL600=1772185455271::auIZejG-Dw50l6x1chl2.3.1772185888003.1; kampyleSessionPageCounter=6; aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod={%22recordingID%22:%226-019c9e74-c03a-7010-aafd-a24035c0a46d%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772185894482%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:%2212.024883669213548%22%2C%22clearsIdentifiedUser%22:false}; aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod={%22heartbeat%22:1772185894482}; _ga_3Q3YNGZLDP=GS2.1.s1772184997$o3$g1$t1772185895$j43$l0$h189743630; aisles-online-state=Fe26.2**d254e747469d72182fa6a181a34d2f6f46b4b9f5276d6b737b75dfc6c3a4aa94*Y-ni23Y4KDcjNBpIeC4KMg*EPNwh_5b8Ji3QQebbXA0fF_CqqcDYicKkWwYvNLDFp2DzGfoasjkF6V7vLnaOLE3**902eae28f3f582d471b5420075cb90bcdd2a90e8108dd7784ead8e7357a77fa0*lG06avFjTgL9IY0HSBWwqUlHUzr0GYfsqG7yZtHjP_A',
}

json_data = {
    'operationName': 'GetProductsAndFiltersFromElasticsearch',
    'variables': {
        'input': {
            'aisleId': '22abadb79c26407fb9e6908a56b63334',
            'includeMto': True,
            'includeWicFilter': True,
            'numberOfSponsoredProductsPerPage': 6,
            'pageInfoInput': {
                'page': 1,
                'pageSize': 60,
            },
            'searchFilterInput': [],
            'searchTerm': 'milk',
            'sortDirection': 'RELEVANCE',
            'spellCorrect': True,
            'storeId': 1759,
        },
        'ipAddress': '45.114.65.131',
        'sessionId': '44c79014-07a6-4d0f-b2d0-3c41cbff2d99',
        'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'pageViewId': '7c7ded82-534c-4b86-b21d-297d44242eb9',
    },
    'query': 'query GetProductsAndFiltersFromElasticsearch($input: AislesOnlineSearchInput!, $sessionId: String, $userAgent: String, $ipAddress: String, $pageViewId: String) {\n  searchProductsResultV2(\n    searchInput: $input\n    sessionId: $sessionId\n    userAgent: $userAgent\n    ipAddress: $ipAddress\n    pageViewId: $pageViewId\n  ) {\n    correctedQuery\n    responseId\n    searchProducts {\n      fuelSaverAmount\n      isBuyAgain\n      isPersonalized\n      onSale\n      price\n      productId\n      responseProductId\n      storeProductId\n      adId\n      basePrice\n      basePriceMultiple\n      priceMultiple\n      sponsored\n      slotTypeId\n      shelfProductId\n      isSponsored\n      adTrackingId\n      __typename\n    }\n    searchFilters {\n      id\n      name\n      searchFilterOptions {\n        id\n        name\n        count\n        __typename\n      }\n      __typename\n    }\n    categories {\n      id\n      name\n      imageUrl\n      __typename\n    }\n    pageInfo {\n      page\n      pageSize\n      hasNextPage\n      totalCount\n      totalPages\n      __typename\n    }\n    __typename\n  }\n}\n',
}

response = requests.post(
    "https://www.hy-vee.com/aisles-online/api/graphql/two-legged/GetProductsAndFiltersFromElasticsearch",
    headers=headers,
    json=json_data,
    impersonate="chrome120"
)

print("Status Code:", response.status_code)

if response.status_code != 200:
    print(response.text)
    exit()

# ==============================
# 4️⃣ JSON Parse
# ==============================

data = response.json()

products = data["data"]["searchProductsResultV2"]["searchProducts"]

print(f"Total Products Fetched: {len(products)}")

# ==============================
# 5️⃣ Extract Required Fields
# ==============================

records = []

for item in products:
    record = {
        "productId": item.get("productId"),
        "price": item.get("price"),
    }
    records.append(record)

df = pd.DataFrame(records)

output_folder = "output"
os.makedirs(output_folder, exist_ok=True)

file_path = os.path.join(output_folder, "hyvee_products.xlsx")

df.to_excel(file_path, index=False)

print(f"Data successfully saved to {file_path}")