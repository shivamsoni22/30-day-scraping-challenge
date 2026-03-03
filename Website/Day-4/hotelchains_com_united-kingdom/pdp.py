from curl_cffi import requests

cookies = {
    '_ga': 'GA1.1.925457895.1771827596',
    'cf_clearance': 'G42avEd6d.jdb7psnoKnah5c3cr4EgK8VoLe7N959C4-1771836271-1.2.1.1-Qip6LXFUtmGK2TAgPSy0hHmljE9pARLJ4YXz.yJlrgT3h6WnbzLScKJyB8cxJReqIf411fb4c0KeqRvpttf133oQy2CUB.mVrqDP.74bf6u5XKEe7rMHbY2X2ikt7llvwjMMERXBctNbavg_0pnw_fBQKzCcufH.0REtIDi8OZ2jR5QulJP.XE_X9xp93QItgUSEE2Uho3AR0BEwwlv99CC3hJXO3o4EMYzWiomV6Gw',
    '_ga_796DWW014E': 'GS2.1.s1771835453$o2$g1$t1771836279$j52$l0$h0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'if-modified-since': 'Thu, 19 Feb 2026 03:53:45 GMT',
    'priority': 'u=0, i',
    'referer': 'https://www.hotelchains.com/united-kingdom/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"145.0.7632.109"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.109", "Chromium";v="145.0.7632.109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'cookie': '_ga=GA1.1.925457895.1771827596; cf_clearance=G42avEd6d.jdb7psnoKnah5c3cr4EgK8VoLe7N959C4-1771836271-1.2.1.1-Qip6LXFUtmGK2TAgPSy0hHmljE9pARLJ4YXz.yJlrgT3h6WnbzLScKJyB8cxJReqIf411fb4c0KeqRvpttf133oQy2CUB.mVrqDP.74bf6u5XKEe7rMHbY2X2ikt7llvwjMMERXBctNbavg_0pnw_fBQKzCcufH.0REtIDi8OZ2jR5QulJP.XE_X9xp93QItgUSEE2Uho3AR0BEwwlv99CC3hJXO3o4EMYzWiomV6Gw; _ga_796DWW014E=GS2.1.s1771835453$o2$g1$t1771836279$j52$l0$h0',
}

response = requests.get('https://www.hotelchains.com/holiday-inn-hotels-resorts/',
                         cookies=cookies,
                        headers=headers,
                        impersonate = 'chrome120'

)

print(response.text)
print(response.status_code)