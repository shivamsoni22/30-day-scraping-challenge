import pandas as pd
import requests
import time

excel_path = r"D:\30-day-scraping-challenge\Website\day-7\hy-vee_com\output\hyvee_products.xlsx"

df = pd.read_excel(excel_path)

df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace("\ufeff", "", regex=False)

if "productId" not in df.columns:
    raise Exception(f"Available columns: {df.columns.tolist()}")

product_ids = (
    df["productId"]
    .dropna()
    .astype(int)
    .unique()
    .tolist()
)

print("Total IDs:", len(product_ids))
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
    'com.silverpop.iMA.session': '58a07650-3b17-9c1a-e896-29baa4d887de',
    '__cf_bm': 'Qd4EZKQy5KlrZWrEGdwqdndWDdbvNpy8caFR9XRwX0w-1772185876-1.0.1.1-Gpj6l1qYR.PZhHbQAD_VJR4R7MeByO2fwNwA3QuqPpMwx2K4dcnP1dr_ntkunscDhEMWST_pxbcmKEb_K3UQK7bV3aysfKdnqR7wCru8OaQ',
    'com.silverpop.iMA.page_visit': '-1454635165:-1043156171:-1729006372:',
    'cf_clearance': 'PZ1RGGYLArP6_LleZBg9hjeTI9zeM2OVAjM9dnYgKdM-1772186465-1.2.1.1-YvqofsX.bgXOYGPIfr1jXH6vKZMGUH.fSap6IOpwo6G2r_laCS_d7vejEV1F9QyKU2o3l12p_kUmuCyM5blS6MM7YTx4LBintyhWiiyHre9cRFSVx43X_zcraK_FA8dVyvUeWvhkJx3SGv9TZXw5G3jZ1GnY7wFTYtQ.447sdeIHg4vLKErmMppCTxeGVclNiLhkV1b184L9JfKuK1USnB.WFv0YaIK_d7F9.zdrDDk',
    'my-account-state': 'Fe26.2**5becd28bbff39fe0b0c9660fc5d38040e3eb125e832d193178a2c1e110b13b2f*NPdzIPua8hPg7U6LRXXMjg*x0fKdxvjVYL-upFffcLgf1-_b3whzQFJNHyzr-dSKlZv0D_3ECVKptT0ffHYoUnY**be6872efbe404fc56e15adfdc0ac0dffeadf2b9fdeff7918280b1898a7f48c3c*vp_5UCr3e1_5ISBakhkXBc2TOtnAJl1oDHXjB-yC_0A',
    '.ASPXANONYMOUS': 'CLEL1WHe3AEkAAAAYzFjOWQ3M2EtNTczMS00NWFhLThmZWYtN2UzOThlNTdlMDQ4Xl8hfQZ6tOUtL1JE3651QRICneU1',
    'ASP.NET_SessionId': 'ea0gevy31f3ugc5vmirz3l4s',
    'unleashSessionId': '409b4858-1762-437c-bd27-c46112a46c60',
    'BIGipServer~Web_Administrators~Hy-Vee.com_PROD.app~Hy-Vee.com_PROD_pool': '!ReikBf+xN6jiTiN4QmxZpmwNFKlAz+3Yh4FWMbufz6AnQcLKiVMudZRXicDfqThvg/xYpdtdQDsZ0w==',
    'lastRskxRun': '1772186469453',
    'ttcsid': '1772185455271::2tedkdDwuYLhG9-53fO9.3.1772186470049.0',
    'ttcsid_C9JGOSJC77U3SHFPL600': '1772185455271::auIZejG-Dw50l6x1chl2.3.1772186470049.1',
    'kampyleSessionPageCounter': '8',
    'aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod': '{%22recordingID%22:%226-019c9e74-c03a-7010-aafd-a24035c0a46d%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772186488560%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:%2212.024883669213548%22%2C%22clearsIdentifiedUser%22:false}',
    'aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod': '{%22heartbeat%22:1772186488561}',
    'aisles-online-state': 'Fe26.2**53275eeb9d69fe5d05900ca1e43a44cf6980a88e914ab8a6d6b04f1c09028e29*QLGkn1qHPXlyDpwVv1lNWA*7XlKlvPvD0q81kg2ZaHuR9XTrcC-ccWskS7pblxi-8PD19X1_12oC3E3mWFuyajX**6d026e1628ef855b86188361a2ffade3c7f1725d2d5c52bb355135158f9fdc95*IE34ZLORH3XyVJDkenfYTRfMbAHO9KI1kyt0k6br_bc',
    '_ga_3Q3YNGZLDP': 'GS2.1.s1772184997$o3$g1$t1772186490$j36$l0$h1176978662',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Feb+27+2026+15%3A31%3A31+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IN%3BGJ',
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
    'x-hy-vee-correlation-id': '24a67771-7211-4edd-9f4d-ddc08d735c5a',
    'x-operation-name': 'LoadSearchProductsForProductCardsQuery',
    # 'cookie': '_pin_unauth=dWlkPU5UZGxOemcwTUdFdE4ySmpNQzAwTjJGaExUbGxZVEV0TXpFMVpXSTFOREZrWkdWaQ; com.silverpop.iMAWebCookie=4de9165b-086e-7ae2-8947-2528ba29b062; _gcl_au=1.1.980378843.1772112454; _ga=GA1.1.1275940071.1772112454; hyveeSessionId=44c79014-07a6-4d0f-b2d0-3c41cbff2d99; _tt_enable_cookie=1; _ttp=01KJD24941ZCCEPN1JM754YBPY_.tt.1; _fbp=fb.1.1772112456070.538203930757108244; rskxRunCookie=0; rCookie=ikf54kuof98dq5bnhahqlmm3i0fk3; BIGipServer~Web_Administrators~Shared_VPC_pool=!2aRfy4bzqCSm+xZ4QmxZpmwNFKlAz3UZt9Qp9BE5fn1Z0o+B8apo4FpH/VfYmfhJwapsOfJMWkgQ/g==; store=%257B%2522address%2522%253A%25228701%2520Douglas%2520Avenue%2522%252C%2522city%2522%253A%2522Urbandale%2522%252C%2522latitude%2522%253A41.6294%252C%2522longitude%2522%253A-93.7369%252C%2522name%2522%253A%2522Urbandale%2522%252C%2522state%2522%253A%2522Iowa%2522%252C%2522storeId%2522%253A%25221759%2522%252C%2522zip%2522%253A%252250322%2522%257D; __Host-hy-vee-main-hy-vee-auth.csrf-token=dd6a1c5bb0b311b554dc539b2d7d5d16585a9bab5fbbcd5295486e41a43e4263%7C83410a2c520ce5e7fb10a2cc604c9eaf65c77a1baee6578c596fa06ba17b3f8a; __Secure-hy-vee-main-hy-vee-auth.callback-url=https%3A%2F%2Fwww.hy-vee.com; navigation=aisles; kampyle_userid=3eb0-e365-a738-4049-9154-e62f-9c28-570a; kampyleUserSession=1772172371160; kampyleUserSessionsCount=1; kampyleUserPercentile=55.139992279846325; com.silverpop.iMA.session=58a07650-3b17-9c1a-e896-29baa4d887de; __cf_bm=Qd4EZKQy5KlrZWrEGdwqdndWDdbvNpy8caFR9XRwX0w-1772185876-1.0.1.1-Gpj6l1qYR.PZhHbQAD_VJR4R7MeByO2fwNwA3QuqPpMwx2K4dcnP1dr_ntkunscDhEMWST_pxbcmKEb_K3UQK7bV3aysfKdnqR7wCru8OaQ; com.silverpop.iMA.page_visit=-1454635165:-1043156171:-1729006372:; cf_clearance=PZ1RGGYLArP6_LleZBg9hjeTI9zeM2OVAjM9dnYgKdM-1772186465-1.2.1.1-YvqofsX.bgXOYGPIfr1jXH6vKZMGUH.fSap6IOpwo6G2r_laCS_d7vejEV1F9QyKU2o3l12p_kUmuCyM5blS6MM7YTx4LBintyhWiiyHre9cRFSVx43X_zcraK_FA8dVyvUeWvhkJx3SGv9TZXw5G3jZ1GnY7wFTYtQ.447sdeIHg4vLKErmMppCTxeGVclNiLhkV1b184L9JfKuK1USnB.WFv0YaIK_d7F9.zdrDDk; my-account-state=Fe26.2**5becd28bbff39fe0b0c9660fc5d38040e3eb125e832d193178a2c1e110b13b2f*NPdzIPua8hPg7U6LRXXMjg*x0fKdxvjVYL-upFffcLgf1-_b3whzQFJNHyzr-dSKlZv0D_3ECVKptT0ffHYoUnY**be6872efbe404fc56e15adfdc0ac0dffeadf2b9fdeff7918280b1898a7f48c3c*vp_5UCr3e1_5ISBakhkXBc2TOtnAJl1oDHXjB-yC_0A; .ASPXANONYMOUS=CLEL1WHe3AEkAAAAYzFjOWQ3M2EtNTczMS00NWFhLThmZWYtN2UzOThlNTdlMDQ4Xl8hfQZ6tOUtL1JE3651QRICneU1; ASP.NET_SessionId=ea0gevy31f3ugc5vmirz3l4s; unleashSessionId=409b4858-1762-437c-bd27-c46112a46c60; BIGipServer~Web_Administrators~Hy-Vee.com_PROD.app~Hy-Vee.com_PROD_pool=!ReikBf+xN6jiTiN4QmxZpmwNFKlAz+3Yh4FWMbufz6AnQcLKiVMudZRXicDfqThvg/xYpdtdQDsZ0w==; lastRskxRun=1772186469453; ttcsid=1772185455271::2tedkdDwuYLhG9-53fO9.3.1772186470049.0; ttcsid_C9JGOSJC77U3SHFPL600=1772185455271::auIZejG-Dw50l6x1chl2.3.1772186470049.1; kampyleSessionPageCounter=8; aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod={%22recordingID%22:%226-019c9e74-c03a-7010-aafd-a24035c0a46d%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772186488560%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:%2212.024883669213548%22%2C%22clearsIdentifiedUser%22:false}; aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod={%22heartbeat%22:1772186488561}; aisles-online-state=Fe26.2**53275eeb9d69fe5d05900ca1e43a44cf6980a88e914ab8a6d6b04f1c09028e29*QLGkn1qHPXlyDpwVv1lNWA*7XlKlvPvD0q81kg2ZaHuR9XTrcC-ccWskS7pblxi-8PD19X1_12oC3E3mWFuyajX**6d026e1628ef855b86188361a2ffade3c7f1725d2d5c52bb355135158f9fdc95*IE34ZLORH3XyVJDkenfYTRfMbAHO9KI1kyt0k6br_bc; _ga_3Q3YNGZLDP=GS2.1.s1772184997$o3$g1$t1772186490$j36$l0$h1176978662; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+27+2026+15%3A31%3A31+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=IN%3BGJ',
}
BATCH_SIZE = 40
all_data = []

for i in range(0, len(product_ids), BATCH_SIZE):

    batch = product_ids[i:i+BATCH_SIZE]

    payload = {
        "operationName": "LoadSearchProductsForProductCardsQuery",
        "variables": {
            "whereIds": batch,
            "storeId": 1759,
            "pageSize": len(batch),
            "pickupLocationHasLocker": False,
            "targeted": False,
            "retailItemEnabled": True,
            "locationIds": [],
            "wicEnabled": True,
            "foodHealthScoreEnabled": False
        },
        "query": """
        query LoadSearchProductsForProductCardsQuery($whereIds: [Int!], $storeId: Int!, $pageSize: Int!, $pickupLocationHasLocker: Boolean!) {
          products(pageSize: $pageSize, whereIds: $whereIds) {
            products {
              productId
              name
              size
              upc
              brandName
              storeProduct(storeId: $storeId, isActive: true) {
                storeProductId
                price
                basePrice
                onSale
                isActive
                insertDate
              }
            }
          }
        }
        """
    }

    response = requests.post(
        "https://www.hy-vee.com/aisles-online/api/graphql/two-legged/LoadSearchProductsForProductCardsQuery",
        headers=headers,
        json=payload,
        timeout=30
    )

    if response.status_code != 200:
        continue

    data = response.json()
    products = data.get("data", {}).get("products", {}).get("products", [])

    for item in products:
        store = item.get("storeProduct") or {}
        all_data.append({
            "Url" : "https://www.hy-vee.com/aisles-online/p/" +item.get("productId"),
            "productId": item.get("productId"),
            "name": item.get("name"),
            "size": item.get("size"),
            "upc": item.get("upc"),
            "brandName": item.get("brandName"),
            "storeProductId": store.get("storeProductId"),
            "price": store.get("price"),
            "basePrice": store.get("basePrice"),
            "onSale": store.get("onSale"),
            "isActive": store.get("isActive"),
            "insertDate": store.get("insertDate"),

        })

    time.sleep(2)

output_path = r"D:\30-day-scraping-challenge\Website\day-7\hy-vee_com\output\hyvee_scraped_output.xlsx"

pd.DataFrame(all_data).to_excel(output_path, index=False)