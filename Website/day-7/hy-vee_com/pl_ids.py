import requests

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
    '__cf_bm': 'HShW_EVBfC0ZG77CGykvodOYcCGBObaiwBpvOKGjo6Q-1772172342-1.0.1.1-7PFvm8jeCLe54b_UB6rW.4Fl3yPgY.qVCQA9UOP3c.wluEDFE6mp35pTGNHpTrKz74pVUN9zqQ0FliAR46MhTRjGLzs9SRfvFVrlkuY1q20',
    'cf_clearance': 'oyJQkFAy.SH9aoRDaRWuSzptxnK4SQ0Q1S5qfZkUnUo-1772172343-1.2.1.1-hs3zg3F93WaRyX3kUSArqu6uxs2Dq0Ii5RcDUWcWP5GUYBN4szx6VKcNXKOQmifTDjFiTYUsNV4pGq6rObBivOn9KEY3zkSZHuStgggSCVwS031act1iB1pQeNsbjh1N4x8vXXQoUeCAMAI4w0OWFoK91S5YFeXaNj3Ulu1ONWALjuYHXEFcV23BNkoKiPk2MlNVJjRL7wUtZmRrstHPnMZqSNjyY9MkGdPoYTHygvI',
    'store': '%257B%2522address%2522%253A%25228701%2520Douglas%2520Avenue%2522%252C%2522city%2522%253A%2522Urbandale%2522%252C%2522latitude%2522%253A41.6294%252C%2522longitude%2522%253A-93.7369%252C%2522name%2522%253A%2522Urbandale%2522%252C%2522state%2522%253A%2522Iowa%2522%252C%2522storeId%2522%253A%25221759%2522%252C%2522zip%2522%253A%252250322%2522%257D',
    '__Host-hy-vee-main-hy-vee-auth.csrf-token': 'dd6a1c5bb0b311b554dc539b2d7d5d16585a9bab5fbbcd5295486e41a43e4263%7C83410a2c520ce5e7fb10a2cc604c9eaf65c77a1baee6578c596fa06ba17b3f8a',
    '__Secure-hy-vee-main-hy-vee-auth.callback-url': 'https%3A%2F%2Fwww.hy-vee.com',
    'com.silverpop.iMA.session': '23578c80-d5cc-e705-5dad-8dc285d5e05b',
    'navigation': 'aisles',
    'com.silverpop.iMA.page_visit': '-1043156171:47:',
    'kampyle_userid': '3eb0-e365-a738-4049-9154-e62f-9c28-570a',
    'kampyleUserSession': '1772172371160',
    'kampyleUserSessionsCount': '1',
    'kampyleUserPercentile': '55.139992279846325',
    'aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod': '{%22heartbeat%22:1772172389207}',
    'aisles-online-state': 'Fe26.2**cf09d77eeac753cc3e1ba69b94449f099fac9fa3d9cd656d65a485577cf536db*i6ujMdubCZGvd6B02Imi_g*L6pNOK9ZZW5xZZxvgYz4PkgVXVSmqnpVhrXjbiquF35UY4j6Y7089_nM6WcL8Lag**5c62102f07f368113cfc6158b52fec39efa56c6c0ebc0ac99903016441c04e35*v0yGSGwW2it1vXRaD_5ZsM36idzLfXZfO5ezIT3e4EQ',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Fri+Feb+27+2026+11%3A36%3A32+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false',
    'lastRskxRun': '1772172394426',
    'kampyleSessionPageCounter': '2',
    '_ga_3Q3YNGZLDP': 'GS2.1.s1772172344$o2$g1$t1772172441$j46$l0$h0',
    'aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod': '{%22recordingID%22:%226-019c9db3-f984-7dda-b280-0e153731cd27%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772172446161%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:12.024883669213548%2C%22clearsIdentifiedUser%22:false}',
    'ttcsid_C9JGOSJC77U3SHFPL600': '1772172346013::I39MMC6VvlgwF4QEy6qE.2.1772172451162.1',
    'ttcsid': '1772172346014::KuWTU-ykM3j3eD94-KYf.2.1772172451162.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'apollographql-client-name': 'aisles-online-web',
    'content-type': 'application/json',
    'origin': 'https://www.hy-vee.com',
    'priority': 'u=1, i',
    'referer': 'https://www.hy-vee.com/aisles-online/search?search=egg&spellCorrect=true&page=2',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-hy-vee-correlation-id': '3051df1a-89c5-41fe-a0e4-ede8de334d17',
    'x-operation-name': 'GetProductsAndFiltersFromElasticsearch',
    # 'cookie': '_pin_unauth=dWlkPU5UZGxOemcwTUdFdE4ySmpNQzAwTjJGaExUbGxZVEV0TXpFMVpXSTFOREZrWkdWaQ; com.silverpop.iMAWebCookie=4de9165b-086e-7ae2-8947-2528ba29b062; _gcl_au=1.1.980378843.1772112454; _ga=GA1.1.1275940071.1772112454; hyveeSessionId=44c79014-07a6-4d0f-b2d0-3c41cbff2d99; _tt_enable_cookie=1; _ttp=01KJD24941ZCCEPN1JM754YBPY_.tt.1; _fbp=fb.1.1772112456070.538203930757108244; rskxRunCookie=0; rCookie=ikf54kuof98dq5bnhahqlmm3i0fk3; BIGipServer~Web_Administrators~Shared_VPC_pool=!2aRfy4bzqCSm+xZ4QmxZpmwNFKlAz3UZt9Qp9BE5fn1Z0o+B8apo4FpH/VfYmfhJwapsOfJMWkgQ/g==; __cf_bm=HShW_EVBfC0ZG77CGykvodOYcCGBObaiwBpvOKGjo6Q-1772172342-1.0.1.1-7PFvm8jeCLe54b_UB6rW.4Fl3yPgY.qVCQA9UOP3c.wluEDFE6mp35pTGNHpTrKz74pVUN9zqQ0FliAR46MhTRjGLzs9SRfvFVrlkuY1q20; cf_clearance=oyJQkFAy.SH9aoRDaRWuSzptxnK4SQ0Q1S5qfZkUnUo-1772172343-1.2.1.1-hs3zg3F93WaRyX3kUSArqu6uxs2Dq0Ii5RcDUWcWP5GUYBN4szx6VKcNXKOQmifTDjFiTYUsNV4pGq6rObBivOn9KEY3zkSZHuStgggSCVwS031act1iB1pQeNsbjh1N4x8vXXQoUeCAMAI4w0OWFoK91S5YFeXaNj3Ulu1ONWALjuYHXEFcV23BNkoKiPk2MlNVJjRL7wUtZmRrstHPnMZqSNjyY9MkGdPoYTHygvI; store=%257B%2522address%2522%253A%25228701%2520Douglas%2520Avenue%2522%252C%2522city%2522%253A%2522Urbandale%2522%252C%2522latitude%2522%253A41.6294%252C%2522longitude%2522%253A-93.7369%252C%2522name%2522%253A%2522Urbandale%2522%252C%2522state%2522%253A%2522Iowa%2522%252C%2522storeId%2522%253A%25221759%2522%252C%2522zip%2522%253A%252250322%2522%257D; __Host-hy-vee-main-hy-vee-auth.csrf-token=dd6a1c5bb0b311b554dc539b2d7d5d16585a9bab5fbbcd5295486e41a43e4263%7C83410a2c520ce5e7fb10a2cc604c9eaf65c77a1baee6578c596fa06ba17b3f8a; __Secure-hy-vee-main-hy-vee-auth.callback-url=https%3A%2F%2Fwww.hy-vee.com; com.silverpop.iMA.session=23578c80-d5cc-e705-5dad-8dc285d5e05b; navigation=aisles; com.silverpop.iMA.page_visit=-1043156171:47:; kampyle_userid=3eb0-e365-a738-4049-9154-e62f-9c28-570a; kampyleUserSession=1772172371160; kampyleUserSessionsCount=1; kampyleUserPercentile=55.139992279846325; aHktdmVlLmNvbQ%3D%3D-_lr_hb_-rl00u5%2Fhy-vee-prod={%22heartbeat%22:1772172389207}; aisles-online-state=Fe26.2**cf09d77eeac753cc3e1ba69b94449f099fac9fa3d9cd656d65a485577cf536db*i6ujMdubCZGvd6B02Imi_g*L6pNOK9ZZW5xZZxvgYz4PkgVXVSmqnpVhrXjbiquF35UY4j6Y7089_nM6WcL8Lag**5c62102f07f368113cfc6158b52fec39efa56c6c0ebc0ac99903016441c04e35*v0yGSGwW2it1vXRaD_5ZsM36idzLfXZfO5ezIT3e4EQ; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Feb+27+2026+11%3A36%3A32+GMT%2B0530+(India+Standard+Time)&version=202510.2.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false; lastRskxRun=1772172394426; kampyleSessionPageCounter=2; _ga_3Q3YNGZLDP=GS2.1.s1772172344$o2$g1$t1772172441$j46$l0$h0; aHktdmVlLmNvbQ%3D%3D-_lr_tabs_-rl00u5%2Fhy-vee-prod={%22recordingID%22:%226-019c9db3-f984-7dda-b280-0e153731cd27%22%2C%22sessionID%22:0%2C%22lastActivity%22:1772172446161%2C%22hasActivity%22:true%2C%22confirmed%22:true%2C%22recordingConditionThreshold%22:12.024883669213548%2C%22clearsIdentifiedUser%22:false}; ttcsid_C9JGOSJC77U3SHFPL600=1772172346013::I39MMC6VvlgwF4QEy6qE.2.1772172451162.1; ttcsid=1772172346014::KuWTU-ykM3j3eD94-KYf.2.1772172451162.0',
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
                'page': 2,
                'pageSize': 60,
            },
            'searchFilterInput': [],
            'searchTerm': 'egg',
            'sortDirection': 'RELEVANCE',
            'spellCorrect': True,
            'storeId': 1759,
        },
        'ipAddress': '45.114.65.131',
        'sessionId': '44c79014-07a6-4d0f-b2d0-3c41cbff2d99',
        'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
        'pageViewId': '783b12b9-cebc-4f16-b81b-cd135c91671f',
    },
    'query': 'query GetProductsAndFiltersFromElasticsearch($input: AislesOnlineSearchInput!, $sessionId: String, $userAgent: String, $ipAddress: String, $pageViewId: String) {\n  searchProductsResultV2(\n    searchInput: $input\n    sessionId: $sessionId\n    userAgent: $userAgent\n    ipAddress: $ipAddress\n    pageViewId: $pageViewId\n  ) {\n    correctedQuery\n    responseId\n    searchProducts {\n      fuelSaverAmount\n      isBuyAgain\n      isPersonalized\n      onSale\n      price\n      productId\n      responseProductId\n      storeProductId\n      adId\n      basePrice\n      basePriceMultiple\n      priceMultiple\n      sponsored\n      slotTypeId\n      shelfProductId\n      isSponsored\n      adTrackingId\n      __typename\n    }\n    searchFilters {\n      id\n      name\n      searchFilterOptions {\n        id\n        name\n        count\n        __typename\n      }\n      __typename\n    }\n    categories {\n      id\n      name\n      imageUrl\n      __typename\n    }\n    pageInfo {\n      page\n      pageSize\n      hasNextPage\n      totalCount\n      totalPages\n      __typename\n    }\n    __typename\n  }\n}\n',
}

response = requests.post(
    'https://www.hy-vee.com/aisles-online/api/graphql/two-legged/GetProductsAndFiltersFromElasticsearch',
    # cookies=cookies,
    headers=headers,
    json=json_data,
)


print(response.text)
print(response.status_code)

