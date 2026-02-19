import requests

cookies = {
    'pcm_personalization_disabled': '0',
    'cors_js': '1',
    'bkng_sso_session': 'e30',
    'BJS': '-',
    '_ga': 'GA1.3.180000344.1771483772',
    '_gid': 'GA1.3.1505107856.1771483772',
    '_gid': 'GA1.2.1505107856.1771483772',
    'pcm_consent': 'consentedAt%3D2026-02-19T07%3A59%3A15.389Z%26countryCode%3DIN%26expiresAt%3D2026-08-18T07%3A59%3A15.389Z%26implicit%3Dfalse%26regionCode%3DGJ%26regulation%3Dnone%26legacyRegulation%3Dnone%26consentId%3D07b55020-771b-4632-8519-6125f8202597%26analytical%3Dfalse%26marketing%3Dfalse',
    'pcm_pac': '%5B%22d94357ea3e7ade5325424afcf130d5561dc5da17351b33cabf00f5bd809feb13%22%2C6%5D',
    'bkng_sso_ses': 'eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6IjEvZThZVUFPSTV1dTAwbVlrNmhoNUJaR0FPQ203REU3K2I4YVlBNU0xcUkifV19',
    '__gads': 'ID=e73481b1974fb9b4:T=1771490428:RT=1771490428:S=ALNI_MbGXEwykkm4AlM1pEu-wOuut-gzFw',
    '__gpi': 'UID=0000133c463e4fef:T=1771490428:RT=1771490428:S=ALNI_MZ-cZbNefpK3S9GtFl05xA0Wsek8w',
    '__eoi': 'ID=e25efb3727baab14:T=1771490428:RT=1771490428:S=AA-AfjbWy4xprFTUcUInkHMAip86',
    '_gcl_au': '1.1.132897788.1771490429',
    'bkng_prue': '1',
    '_yjsu_yjad': '1771490430.912c6af6-34f7-4a55-ba6d-961f4a80360c',
    '_uetsid': 'a5acb9100d6e11f1aab263264e5ef1b8',
    '_uetvid': 'a5ad1c000d6e11f1ac672b7e00a8bb66',
    'FPID': 'FPID2.2.3e4eyi5IoLeawCX0uTZd123Dsurbbj9wUjOc59%2BWXnw%3D.1771483772',
    'FPAU': '1.1.132897788.1771490429',
    'FPLC': 'UjkNqKvcG7jFKgruQoVkYVCfqK9gahK8yWqXB6O30dPiVJ8vc9Nfwv1hlxz9JQrZwuRYqDW8I6GkWj%2BHnv%2BkXFG2xuqw2rjS3ztMY1v%2BVkL72JscZ4iTqRJNTMeWZg%3D%3D',
    '_ga_A12345': 'GS2.1.s1771490429$o1$g1$t1771490442$j47$l0$h570329233',
    '_ga': 'GA1.2.180000344.1771483772',
    'cgumid': 'dNd2r18lMkZhNk1WWSUyQkVWR3gxN3BEMEt5Q1pXWWR4UWpEdDgyOXhCZ0dJTmdQa051MHJGTm4lMkZvY0JUV2U2T21sQVNwOVAlMkZjd0xhbTZHZ0Mzb2RKWkJJcGpvc2lBJTNEJTNE',
    'bkng_sso_auth': 'CAIQm8CWywYaeD2JDYal6x0SfXQ8+bOfT6gG8AtOFrrut0g/Xc1jDnt97cfVtJjqEVEkRQYK6DzIT5rDWzBHG0SX4aQlX6hQa/lXjdJAApo26c0OLRPCxX9SfWFrOBP4wttvm117nlN8EDC+GUJhbOriCa+5w5W41+ys5yR4+CkD1w==',
    '_gat': '1',
    'g_state': '{"i_l":0,"i_ll":1771490772975,"i_b":"lK6SoENXwFFhNLIalryOXN5zuP8oKcp3TAF7DJlpZHs","i_e":{"enable_itp_optimization":0}}',
    'cto_bundle': 'ucQ0o183cXZqdFBIdlJBY1hBcXptTXFWN3RiRkJBQyUyRjRlVThSNHp1azBsSjFNcjNjYmJ3anJWY3N5MGJBTW5HZDJxcEhqTzFEWjFTQiUyRlRjNkdPN1U3ZGVSU2I0TlRUaDVoSTRwWTNyYzBaSUlDb0UwQXk1ZmwlMkZ5UWRNcUF0QTZmOTR4WA',
    'bkng': '11UmFuZG9tSVYkc2RlIyh9YfDNyGw8J7nzPnUG3Pr%2Bfv56J3ue4x%2FP5IcJ4wiW7wQnV3uqfVecxDXyHzimv%2BF2j7KCYiu5%2BuR8Tl389IPH2RHWp4YeiH0iBC7fnuuMVTYixgDz8qL1E5SQPMz6epFRdxKVM0Fqm9A1Q6Irji3fFvXfG9TsYOi7xJk8z4%2B%2FdT9G8voFmq3aIWgFjgUpy5ChuQ%3D%3D',
    'aws-waf-token': '4f5efe34-8248-4379-a149-2d7481a36480:BQoAmX88Ue+mAAAA:SK7L46nyIepqGtsjHVNDFmz/XhfqU/7xZyQTn1xPEs4s1DOpg1b07u3YCmoYVNx84nieV0RVO0LSx4DevQveaXDOJz6dvjI9oI2iOeFqFWsLQxNayyNyRGBaO8HOrjdxdi9+wR7kYGCJsQYeSsaNt7oJZTmHWcSDeV8yEfXsP4764OGXtVlod16sVNT94wuyiA6rj+2rqh0FFXl9IlVCkSlwucD68eBUW7fkl6gBtkxOo9yJ83vQz69+hSQraGp+nvM=',
    'OptanonConsent': 'implicitConsentCountry=nonGDPR&implicitConsentDate=1771483770655&isGpcEnabled=0&datestamp=Thu+Feb+19+2026+14%3A16%3A17+GMT%2B0530+(India+Standard+Time)&version=202411.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ea7ecdb1-587b-4156-8ac1-ea202bbf8b71&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fsp.booking.com%2Fhotel%2Fin%2Frajvanshi-inn.html%3Flabel%3Dgen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AvqY28wGwAIB0gIkNmNjYjczMzQtMTA4My00ZDg0LTk3ZTQtMmQ4ZTc4ZDAwZGZj2AIB4AIB%26sid%3Dcc1c15fa99abce41f38751c0919c7c6b%26all_sr_blocks%3D1582215201_429337230_20_1_0%26checkin%3D2026-02-20%26checkout%3D2026-03-18%26dest_id%3D-2088270%26dest_type%3Dcity%26dist%3D0%26group_adults%3D2%26group_children%3D0%26hapos%3D2%26highlighted_blocks%3D1582215201_429337230_20_1_0%26hpos%3D2%26matching_block_id%3D1582215201_429337230_20_1_0%26no_rooms%3D1%26req_adults%3D2%26req_children%3D0%26room1%3DA%252CA%26sb_price_type%3Dtotal%26sr_order%3Dpopularity%26sr_pri_blocks%3D1582215201_429337230_20_1_0__2649790%26srepoch%3D1771490769%26srpvid%3D6c963d0a5d3c043a%26type%3Dtotal%26ucfs%3D1%26&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'ect': '4g',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    # 'cookie': 'pcm_personalization_disabled=0; cors_js=1; bkng_sso_session=e30; BJS=-; _ga=GA1.3.180000344.1771483772; _gid=GA1.3.1505107856.1771483772; _gid=GA1.2.1505107856.1771483772; pcm_consent=consentedAt%3D2026-02-19T07%3A59%3A15.389Z%26countryCode%3DIN%26expiresAt%3D2026-08-18T07%3A59%3A15.389Z%26implicit%3Dfalse%26regionCode%3DGJ%26regulation%3Dnone%26legacyRegulation%3Dnone%26consentId%3D07b55020-771b-4632-8519-6125f8202597%26analytical%3Dfalse%26marketing%3Dfalse; pcm_pac=%5B%22d94357ea3e7ade5325424afcf130d5561dc5da17351b33cabf00f5bd809feb13%22%2C6%5D; bkng_sso_ses=eyJib29raW5nX2dsb2JhbCI6W3siYSI6MSwiaCI6IjEvZThZVUFPSTV1dTAwbVlrNmhoNUJaR0FPQ203REU3K2I4YVlBNU0xcUkifV19; __gads=ID=e73481b1974fb9b4:T=1771490428:RT=1771490428:S=ALNI_MbGXEwykkm4AlM1pEu-wOuut-gzFw; __gpi=UID=0000133c463e4fef:T=1771490428:RT=1771490428:S=ALNI_MZ-cZbNefpK3S9GtFl05xA0Wsek8w; __eoi=ID=e25efb3727baab14:T=1771490428:RT=1771490428:S=AA-AfjbWy4xprFTUcUInkHMAip86; _gcl_au=1.1.132897788.1771490429; bkng_prue=1; _yjsu_yjad=1771490430.912c6af6-34f7-4a55-ba6d-961f4a80360c; _uetsid=a5acb9100d6e11f1aab263264e5ef1b8; _uetvid=a5ad1c000d6e11f1ac672b7e00a8bb66; FPID=FPID2.2.3e4eyi5IoLeawCX0uTZd123Dsurbbj9wUjOc59%2BWXnw%3D.1771483772; FPAU=1.1.132897788.1771490429; FPLC=UjkNqKvcG7jFKgruQoVkYVCfqK9gahK8yWqXB6O30dPiVJ8vc9Nfwv1hlxz9JQrZwuRYqDW8I6GkWj%2BHnv%2BkXFG2xuqw2rjS3ztMY1v%2BVkL72JscZ4iTqRJNTMeWZg%3D%3D; _ga_A12345=GS2.1.s1771490429$o1$g1$t1771490442$j47$l0$h570329233; _ga=GA1.2.180000344.1771483772; cgumid=dNd2r18lMkZhNk1WWSUyQkVWR3gxN3BEMEt5Q1pXWWR4UWpEdDgyOXhCZ0dJTmdQa051MHJGTm4lMkZvY0JUV2U2T21sQVNwOVAlMkZjd0xhbTZHZ0Mzb2RKWkJJcGpvc2lBJTNEJTNE; bkng_sso_auth=CAIQm8CWywYaeD2JDYal6x0SfXQ8+bOfT6gG8AtOFrrut0g/Xc1jDnt97cfVtJjqEVEkRQYK6DzIT5rDWzBHG0SX4aQlX6hQa/lXjdJAApo26c0OLRPCxX9SfWFrOBP4wttvm117nlN8EDC+GUJhbOriCa+5w5W41+ys5yR4+CkD1w==; _gat=1; g_state={"i_l":0,"i_ll":1771490772975,"i_b":"lK6SoENXwFFhNLIalryOXN5zuP8oKcp3TAF7DJlpZHs","i_e":{"enable_itp_optimization":0}}; cto_bundle=ucQ0o183cXZqdFBIdlJBY1hBcXptTXFWN3RiRkJBQyUyRjRlVThSNHp1azBsSjFNcjNjYmJ3anJWY3N5MGJBTW5HZDJxcEhqTzFEWjFTQiUyRlRjNkdPN1U3ZGVSU2I0TlRUaDVoSTRwWTNyYzBaSUlDb0UwQXk1ZmwlMkZ5UWRNcUF0QTZmOTR4WA; bkng=11UmFuZG9tSVYkc2RlIyh9YfDNyGw8J7nzPnUG3Pr%2Bfv56J3ue4x%2FP5IcJ4wiW7wQnV3uqfVecxDXyHzimv%2BF2j7KCYiu5%2BuR8Tl389IPH2RHWp4YeiH0iBC7fnuuMVTYixgDz8qL1E5SQPMz6epFRdxKVM0Fqm9A1Q6Irji3fFvXfG9TsYOi7xJk8z4%2B%2FdT9G8voFmq3aIWgFjgUpy5ChuQ%3D%3D; aws-waf-token=4f5efe34-8248-4379-a149-2d7481a36480:BQoAmX88Ue+mAAAA:SK7L46nyIepqGtsjHVNDFmz/XhfqU/7xZyQTn1xPEs4s1DOpg1b07u3YCmoYVNx84nieV0RVO0LSx4DevQveaXDOJz6dvjI9oI2iOeFqFWsLQxNayyNyRGBaO8HOrjdxdi9+wR7kYGCJsQYeSsaNt7oJZTmHWcSDeV8yEfXsP4764OGXtVlod16sVNT94wuyiA6rj+2rqh0FFXl9IlVCkSlwucD68eBUW7fkl6gBtkxOo9yJ83vQz69+hSQraGp+nvM=; OptanonConsent=implicitConsentCountry=nonGDPR&implicitConsentDate=1771483770655&isGpcEnabled=0&datestamp=Thu+Feb+19+2026+14%3A16%3A17+GMT%2B0530+(India+Standard+Time)&version=202411.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=ea7ecdb1-587b-4156-8ac1-ea202bbf8b71&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fsp.booking.com%2Fhotel%2Fin%2Frajvanshi-inn.html%3Flabel%3Dgen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AvqY28wGwAIB0gIkNmNjYjczMzQtMTA4My00ZDg0LTk3ZTQtMmQ4ZTc4ZDAwZGZj2AIB4AIB%26sid%3Dcc1c15fa99abce41f38751c0919c7c6b%26all_sr_blocks%3D1582215201_429337230_20_1_0%26checkin%3D2026-02-20%26checkout%3D2026-03-18%26dest_id%3D-2088270%26dest_type%3Dcity%26dist%3D0%26group_adults%3D2%26group_children%3D0%26hapos%3D2%26highlighted_blocks%3D1582215201_429337230_20_1_0%26hpos%3D2%26matching_block_id%3D1582215201_429337230_20_1_0%26no_rooms%3D1%26req_adults%3D2%26req_children%3D0%26room1%3DA%252CA%26sb_price_type%3Dtotal%26sr_order%3Dpopularity%26sr_pri_blocks%3D1582215201_429337230_20_1_0__2649790%26srepoch%3D1771490769%26srpvid%3D6c963d0a5d3c043a%26type%3Dtotal%26ucfs%3D1%26&groups=C0001%3A1%2CC0002%3A1%2CC0004%3A1',
}

response = requests.get(
    'https://sp.booking.com/hotel/in/rajvanshi-inn.html?label=gen173nr-10CAEoggI46AdIM1gEaGyIAQGYATO4ARfIAQzYAQPoAQH4AQGIAgGoAgG4AvqY28wGwAIB0gIkNmNjYjczMzQtMTA4My00ZDg0LTk3ZTQtMmQ4ZTc4ZDAwZGZj2AIB4AIB&sid=cc1c15fa99abce41f38751c0919c7c6b&all_sr_blocks=1582215201_429337230_20_1_0&checkin=2026-02-20&checkout=2026-03-18&dest_id=-2088270&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=2&highlighted_blocks=1582215201_429337230_20_1_0&hpos=2&matching_block_id=1582215201_429337230_20_1_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=1582215201_429337230_20_1_0__2649790&srepoch=1771490769&srpvid=6c963d0a5d3c043a&type=total&ucfs=1&',
    cookies=cookies,
    headers=headers,
)
print(response.text)
print(response.status_code)