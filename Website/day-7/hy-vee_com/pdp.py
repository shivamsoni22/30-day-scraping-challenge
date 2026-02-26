import jmespath
from curl_cffi import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

cookies = {
    'BIGipServer~Web_Administrators~Shared_VPC_pool': '!HaK4Ere1GTIiaZ54QmxZpmwNFKlAzwa0onTygmym0ciHpeQ2osYAML1bq4d7SkcjgAIab0ujz0F78g==',
    '__cf_bm': 'UB.mKXpJHPJfArUGBNk4uf.SinKBBasDB0ZJSYSFG5o-1772112451-1.0.1.1-Znu6zseE6oFaYMbUIkLAuPyPpcMW5m8_L0.u6C6PhSjS.VW1UR9owdnEwRVOR1A_tpDon.aG4ohlLk3F3srZ57o0eu2C2LKnp6QVmQWYz9Q',
    'cf_clearance': 'Bk5iotFNPEDHR8zrSPky.fRxpwMBvJu2mkA76kmZYt4-1772112452-1.2.1.1-c49fHd.8yOzEaI8nw28ntONKcScZTbPyFAA5IjOTk0vRKzrzEGQm.OHTdWdol2LwovD91LMqsYrRchrtc7GaRemSFmafcLEbGLlrEc1SAnN61fwlbkWkHYdFT0vCZTFb6dT1UlwiyNke.ScwwB4PlFiUhNj9y5rWALSpodaD7t4fmfDuVOxTlBNO24TGRML_s4wUTO1LABv_aF3otbClFW_ZUy118lP9glY5kigFSio',
    'store': '%257B%2522address%2522%253A%25228701%2520Douglas%2520Avenue%2522%252C%2522city%2522%253A%2522Urbandale%2522%252C%2522latitude%2522%253A41.6294%252C%2522longitude%2522%253A-93.7369%252C%2522name%2522%253A%2522Urbandale%2522%252C%2522state%2522%253A%2522Iowa%2522%252C%2522storeId%2522%253A%25221759%2522%252C%2522zip%2522%253A%252250322%2522%257D',
    '_pin_unauth': 'dWlkPU5UZGxOemcwTUdFdE4ySmpNQzAwTjJGaExUbGxZVEV0TXpFMVpXSTFOREZrWkdWaQ',
    'com.silverpop.iMAWebCookie': '4de9165b-086e-7ae2-8947-2528ba29b062',
    'com.silverpop.iMA.session': '1070ce42-74e0-92d1-4201-4caee6247867',
    '__Host-hy-vee-main-hy-vee-auth.csrf-token': '465f0a895c251d3e17228d5fd619310275e7a4b62863a45b32e8fe9aae05dbaa%7C8e05788504456ca67058178d2cdcc6009a98a155818964e2fe8f9054d73780c8',
    '__Secure-hy-vee-main-hy-vee-auth.callback-url': 'https%3A%2F%2Fwww.hy-vee.com',
    '_gcl_au': '1.1.980378843.1772112454',
    '_ga': 'GA1.1.1275940071.1772112454',
    'hyveeSessionId': '44c79014-07a6-4d0f-b2d0-3c41cbff2d99',
    '_tt_enable_cookie': '1',
    '_ttp': '01KJD24941ZCCEPN1JM754YBPY_.tt.1',
    '_fbp': 'fb.1.1772112456070.538203930757108244',
    'navigation': 'aisles',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Feb+26+2026+18%3A57%3A50+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'com.silverpop.iMA.page_visit': '-807135407:47:',
    'ttcsid': '1772112454790::jOt1swzLdDLgu8RRo3Ow.1.1772112471649.0',
    'ttcsid_C9JGOSJC77U3SHFPL600': '1772112454789::0yKcEvDfuY3DxkI3hnYm.1.1772112471649.1',
    'lastRskxRun': '1772112473280',
    'rskxRunCookie': '0',
    'rCookie': 'ikf54kuof98dq5bnhahqlmm3i0fk3',
    'aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod': '{%22recordingID%22:%226-019c9a22-1cc8-7717-9704-331989cd1a75%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772112507919%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:13.533584182430737%2C%22clearsIdentifiedUser%22:false}',
    'aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod': '{%22heartbeat%22:1772112507919}',
    '_ga_3Q3YNGZLDP': 'GS2.1.s1772112453$o1$g1$t1772112509$j4$l0$h1583732714',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'aisles-online-web',
    'content-type': 'application/json',
    'origin': 'https://www.hy-vee.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hy-vee.com/aisles-online/p/66055/certified-ground-chuck-85-lean-15-fat',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'x-hy-vee-correlation-id': '33151bdf-7f27-4e28-852b-4615b392a807',
    'x-operation-name': 'getProductDetailsWithPrice',
    # 'cookie': 'BIGipServer~Web_Administrators~Shared_VPC_pool=!HaK4Ere1GTIiaZ54QmxZpmwNFKlAzwa0onTygmym0ciHpeQ2osYAML1bq4d7SkcjgAIab0ujz0F78g==; __cf_bm=UB.mKXpJHPJfArUGBNk4uf.SinKBBasDB0ZJSYSFG5o-1772112451-1.0.1.1-Znu6zseE6oFaYMbUIkLAuPyPpcMW5m8_L0.u6C6PhSjS.VW1UR9owdnEwRVOR1A_tpDon.aG4ohlLk3F3srZ57o0eu2C2LKnp6QVmQWYz9Q; cf_clearance=Bk5iotFNPEDHR8zrSPky.fRxpwMBvJu2mkA76kmZYt4-1772112452-1.2.1.1-c49fHd.8yOzEaI8nw28ntONKcScZTbPyFAA5IjOTk0vRKzrzEGQm.OHTdWdol2LwovD91LMqsYrRchrtc7GaRemSFmafcLEbGLlrEc1SAnN61fwlbkWkHYdFT0vCZTFb6dT1UlwiyNke.ScwwB4PlFiUhNj9y5rWALSpodaD7t4fmfDuVOxTlBNO24TGRML_s4wUTO1LABv_aF3otbClFW_ZUy118lP9glY5kigFSio; store=%257B%2522address%2522%253A%25228701%2520Douglas%2520Avenue%2522%252C%2522city%2522%253A%2522Urbandale%2522%252C%2522latitude%2522%253A41.6294%252C%2522longitude%2522%253A-93.7369%252C%2522name%2522%253A%2522Urbandale%2522%252C%2522state%2522%253A%2522Iowa%2522%252C%2522storeId%2522%253A%25221759%2522%252C%2522zip%2522%253A%252250322%2522%257D; _pin_unauth=dWlkPU5UZGxOemcwTUdFdE4ySmpNQzAwTjJGaExUbGxZVEV0TXpFMVpXSTFOREZrWkdWaQ; com.silverpop.iMAWebCookie=4de9165b-086e-7ae2-8947-2528ba29b062; com.silverpop.iMA.session=1070ce42-74e0-92d1-4201-4caee6247867; __Host-hy-vee-main-hy-vee-auth.csrf-token=465f0a895c251d3e17228d5fd619310275e7a4b62863a45b32e8fe9aae05dbaa%7C8e05788504456ca67058178d2cdcc6009a98a155818964e2fe8f9054d73780c8; __Secure-hy-vee-main-hy-vee-auth.callback-url=https%3A%2F%2Fwww.hy-vee.com; _gcl_au=1.1.980378843.1772112454; _ga=GA1.1.1275940071.1772112454; hyveeSessionId=44c79014-07a6-4d0f-b2d0-3c41cbff2d99; _tt_enable_cookie=1; _ttp=01KJD24941ZCCEPN1JM754YBPY_.tt.1; _fbp=fb.1.1772112456070.538203930757108244; navigation=aisles; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Feb+26+2026+18%3A57%3A50+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; com.silverpop.iMA.page_visit=-807135407:47:; ttcsid=1772112454790::jOt1swzLdDLgu8RRo3Ow.1.1772112471649.0; ttcsid_C9JGOSJC77U3SHFPL600=1772112454789::0yKcEvDfuY3DxkI3hnYm.1.1772112471649.1; lastRskxRun=1772112473280; rskxRunCookie=0; rCookie=ikf54kuof98dq5bnhahqlmm3i0fk3; aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod={%22recordingID%22:%226-019c9a22-1cc8-7717-9704-331989cd1a75%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772112507919%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:13.533584182430737%2C%22clearsIdentifiedUser%22:false}; aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod={%22heartbeat%22:1772112507919}; _ga_3Q3YNGZLDP=GS2.1.s1772112453$o1$g1$t1772112509$j4$l0$h1583732714',
}

json_data1 = {
    'operationName': 'getProductDetailsWithPrice',
    'variables': {
        'locationIds': [
            '266a52f4-0e7a-4729-bc6f-25c6ebaca111',
        ],
        'retailItemEnabled': True,
        'targeted': False,
        'wicEnabled': True,
        'foodHealthScoreEnabled': True,
        'pickupLocationHasLocker': False,
        'productId': 66055,
        'storeId': 1759,
    },
    'query': 'query getProductDetailsWithPrice($locationIds: [ID!] = [], $retailItemEnabled: Boolean = false, $productId: Int!, $storeId: Int, $pickupLocationHasLocker: Boolean!, $targeted: Boolean = false, $wicEnabled: Boolean = false, $foodHealthScoreEnabled: Boolean = false) {\n  product(productId: $productId) {\n    productId\n    size\n    productLockers @include(if: $pickupLocationHasLocker) {\n      productLockerId\n      pickupLocationId\n      isLockerEligible\n      __typename\n    }\n    couponProductV4(targeted: $targeted) {\n      couponsV4 {\n        couponId\n        offerState\n        valueText\n        __typename\n      }\n      __typename\n    }\n    item {\n      ecommerceDefaultPrice\n      nutrition @include(if: $foodHealthScoreEnabled) {\n        score\n        activeBoosters {\n          code\n          title\n          value\n          description\n          __typename\n        }\n        activeDetractors {\n          code\n          title\n          value\n          description\n          __typename\n        }\n        __typename\n      }\n      ...IItemFragment\n      retailItems(locationIds: $locationIds) @include(if: $retailItemEnabled) {\n        ...IRetailItemFragment\n        __typename\n      }\n      madeToOrder {\n        mtoItems {\n          mtoModifiers {\n            mtoModifierId\n            options {\n              code\n              amount\n              __typename\n            }\n            __typename\n          }\n          fulfillmentBeginDate\n          fulfillmentEndDate\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  storeProducts(where: {productId: $productId, storeId: $storeId, isActive: true}) {\n    storeProducts {\n      storeProductId\n      productId\n      storeId\n      onSale\n      onFuelSaver\n      isWeighted\n      isAlcohol\n      fuelSaver\n      price\n      priceMultiple\n      basePrice\n      basePriceMultiple\n      isTagPriceLower\n      department {\n        departmentId\n        __typename\n      }\n      storeProductDescriptions {\n        type\n        description\n        __typename\n      }\n      subcategoryId\n      departmentGroup {\n        departmentGroupId\n        linkPath\n        name\n        __typename\n      }\n      department {\n        departmentId\n        linkPath\n        name\n        __typename\n      }\n      category {\n        categoryId\n        departmentId\n        linkPath\n        name\n        subcategories {\n          subcategoryId\n          linkPath\n          name\n          __typename\n        }\n        __typename\n      }\n      variations {\n        name\n        variationsAttributes {\n          name\n          variationsProducts {\n            productId\n            product {\n              productId\n              name\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment IWicItemFragment on WicItem {\n  isCvb\n  isBroadbandAllowed\n  wicExchangeRate\n  wicItemId\n  wicSubcategory {\n    categoryCode\n    categoryDescription\n    subcategoryCode\n    subcategoryDescription\n    unitOfMeasure\n    isBroadbandSubcategory\n    __typename\n  }\n  upcHyVee\n  __typename\n}\n\nfragment IMadeToOrderItemFragment on MtoItem {\n  mtoItemId\n  prepTime\n  fulfillmentBeginDate\n  fulfillmentEndDate\n  messages {\n    name\n    __typename\n  }\n  mtoModifiers {\n    options {\n      amount\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment IItemFragment on Item {\n  itemId\n  description\n  ecommerceStatus\n  source\n  images {\n    imageId\n    url\n    isPrimaryImage\n    __typename\n  }\n  source\n  unitAverageWeight\n  WicItems(locationIds: $locationIds) @include(if: $wicEnabled) {\n    ...IWicItemFragment\n    __typename\n  }\n  madeToOrder {\n    mtoItems {\n      ...IMadeToOrderItemFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment IRetailItemFragment on RetailItem {\n  retailItemId\n  basePrice\n  basePriceQuantity\n  soldByUnitOfMeasure {\n    code\n    name\n    __typename\n  }\n  tagPrice\n  tagPriceQuantity\n  ecommerceTagPrice\n  ecommerceTagPriceQuantity\n  memberTagPrice\n  memberTagPriceQuantity\n  sellingRules\n  __typename\n}\n',
}

# response = requests.post(
#     'https://www.hy-vee.com/aisles-online/api/graphql/two-legged/getProductDetailsWithPrice',
#     # cookies=cookies,
#     headers=headers,
#     json=json_data,
# )

url = 'https://www.hy-vee.com/aisles-online/api/graphql/two-legged/getProductDetailsWithPrice'
def make_request(i):
   try:
       r = requests.post(
           url,
           json=json_data1,
           headers=headers,
           # cookies=cookies,
           impersonate="chrome120",
           timeout=10,
       )
       # json_data = r.json()
       print(r.status_code)
       if 'Certified Ground Chuck 85% Lean 15% Fat' in r.text and  '5.99' in r.text :
           res =  'good response'
           return f"Request {i}   : {res}   "
       else:
           return f"Request {i}  No goods_name"
   except Exception as e:
       return f"Request {i}  Error: {e}"
if __name__ == "__main__":
   num_requests = 3000
   max_workers = 25
   results = []
   with ThreadPoolExecutor(max_workers=max_workers) as executor:
       futures = [executor.submit(make_request, i) for i in range(1, num_requests + 1)]
       for future in as_completed(futures):
           results.append(future.result())
           print(future.result())

