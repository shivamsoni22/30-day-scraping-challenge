from curl_cffi import requests

headers = {
    'Accept': 'application/json',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Origin': 'https://louisphilippe.abfrl.in',
    'Referer': 'https://louisphilippe.abfrl.in/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'device': 'desktop',
    # 'deviceid': '019c7a45-031c-7222-83e5-6bbad183a222',
    # 'devicetoken': '3dbc95393126cb48fb6161bc22e46baa.1771577869',
    # 'devicetype': 'desktop',
    # 'env': 'PROD',
    # 'hash': '60ea2954c32830631782c1fcca436d51',
    'requestBrand': 'SA',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'securekey': '00175e0566c5448c95b0d5e9051a6a00',
    'sessionId': '3dbc95393126cb48fb6161bc22e46baa',
    'shopid': '3',
}

json_data = {
    'brand': 'Louis Philippe',
    'customerId': 0,
    'cartId': 0,
    'fcmToken': '111',
    'version': '1.2',
    'validateHash': False,
    'geoLocation': {
        'latitude': 343,
        'longitude': 343,
    },
    'latitude': '',
    'longitude': '',
    # 'deviceid': '019c7a45-031c-7222-83e5-6bbad183a222',
    # 'devicetoken': '3dbc95393126cb48fb6161bc22e46baa.1771577869',
    # 'hash': 'c8d2640fbef7b5d1395417e7f80392de',
    'sessionId': '3dbc95393126cb48fb6161bc22e46baa',
    'utmSource': 'https://louisphilippe.abfrl.in/p/men-navy-genericfit-textured-flat-front-formal-trousers-40077249.html?source=Complete-The-Look',
    'rcs': '',
    'regionID': 'UL',
    'rid': 'UL',
    'capillaryUserId': '',
    'requestMode': 'recommended',
    'pageName': 'pdp',
    'productId': 40077249,
    'chi': 8866,
    'categoryId': 8866,
    'deviceType': 'desktop',
    'cv': 0,
    'fp': '',
    'sorting': 'popular:asc',
    'limit': 32,
    'offset': 0,
    'pageNo': 1,
    'searchWord': '',
    'categoryName': '',
    'referer': 'https://louisphilippe.abfrl.in/p/men-navy-genericfit-textured-flat-front-formal-trousers-40077249.html?source=Complete-The-Look',
    'deviceId': '019c7a45-031c-7222-83e5-6bbad183a222',
    'deviceToken': '3dbc95393126cb48fb6161bc22e46baa.1771577869',
    'shopId': 3,
}

response = requests.post('https://plpengineapis.abfrl.in/fetchProducts',
                         headers=headers,
                         json=json_data,
                         impersonate='tor145'
                         )



print(response.text)
print(response.status_code)





