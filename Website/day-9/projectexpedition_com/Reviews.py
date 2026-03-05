import requests

cookies = {
    'country': 'US',
    'currency': 'USD',
    'PHPSESSID': 'a7ao4oeavlk8kmpjupcb2akjfm',
    '_ga': 'GA1.2.1351434886.1772518614',
    '_gid': 'GA1.2.56688391.1772518614',
    'rskxRunCookie': '0',
    'rCookie': 'kx4vpkofvkeqqimqrwevumma7tjeo',
    '_ga_LCMB2K4C1C': 'GS2.2.s1772518615$o1$g1$t1772519467$j4$l0$h0',
    'lastRskxRun': '1772519469285',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.projectexpedition.com/location/mexico/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'cookie': 'country=US; currency=USD; PHPSESSID=a7ao4oeavlk8kmpjupcb2akjfm; _ga=GA1.2.1351434886.1772518614; _gid=GA1.2.56688391.1772518614; rskxRunCookie=0; rCookie=kx4vpkofvkeqqimqrwevumma7tjeo; _ga_LCMB2K4C1C=GS2.2.s1772518615$o1$g1$t1772519467$j4$l0$h0; lastRskxRun=1772519469285',
}

response = requests.get(
    'https://www.projectexpedition.com/tour-activity/cabo-san-lucas/los-cabos-luxury-snorkel-and-lunch-cruise/27049/',
    # cookies=cookies,
    headers=headers,
)
re = (response.text).strip(cleanTourActivity)[1].strip()
print(response.text)
print(response.status_code)