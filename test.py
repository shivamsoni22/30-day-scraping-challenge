import requests

cookies = {
    '__Secure-BUCKET': 'CMAH',
    'SEARCH_SAMESITE': 'CgQIl6AB',
    'SID': 'g.a0006whg7TzGS0owvhFG6ERBR2SNFrUtz5JbVfppXV26BG48v0o7iAuT2m5o8vs7j_qa9CDi7QACgYKAQASARMSFQHGX2MiQ-sknxhLblORoKMM75EZnhoVAUF8yKoyP3kzO7tTNClVeNEOd4tr0076',
    '__Secure-1PSID': 'g.a0006whg7TzGS0owvhFG6ERBR2SNFrUtz5JbVfppXV26BG48v0o7HPPRJyPZRT42ihgv24ZlOwACgYKAVQSARMSFQHGX2MiVvgOADSnQTQ26_-7amF4thoVAUF8yKreday_Ser23PCgngWSFnGa0076',
    '__Secure-3PSID': 'g.a0006whg7TzGS0owvhFG6ERBR2SNFrUtz5JbVfppXV26BG48v0o75E9Qmbb_-nBZcsZbOwx9GAACgYKAXUSARMSFQHGX2Mi9utbrEXPLNowrrB3YmnEGxoVAUF8yKr8PCk43hcjZH32gUgFYsGL0076',
    'HSID': 'AEe3bhLYTfLwfdnui',
    'SSID': 'AFv6Qvqp-rGqJBUfS',
    'APISID': 'aniM27_cQhrOhdBb/A_afpNR6XFzWHO9tO',
    'SAPISID': 'BcH3B18EuFt5C0p4/Ad0Rj8yoqNFeVVqgW',
    '__Secure-1PAPISID': 'BcH3B18EuFt5C0p4/Ad0Rj8yoqNFeVVqgW',
    '__Secure-3PAPISID': 'BcH3B18EuFt5C0p4/Ad0Rj8yoqNFeVVqgW',
    '__Secure-ENID': '31.SE=iBKeL1NwrwFh9zQZRdY0vc0QOUXynfdKLQaIsMsf-9NrzQbCCmekD34aau51OrjdA6yan_5s1DGX0xNPeP_QmH5d42PseqgaPcooslTQgCQhkj_2N8rtbPWfhcOCHm3GMCGSUyrFIg9Y3b-zUovs3rnn160l18Ab7A5vl99Jpa9NsXy7jGAaox20ycRPXCorcWkI8RJBmPLZUESWCkMx1bexcMGj-JX_dMx3Z-S92lUFCs5_8G6TPsom0bD9ZxKsCKtP4QVslK3tRqb40FA3OwYUafxxH57BtjJkQ9fNcRsmXhQ1w1tZWhk1QAUFxJbbY7NX-2-GL9ZBXSI',
    'AEC': 'AaJma5vuohRnoycKcyBfinvX_ww8ZcsH2OKlgYtC8FIKWwsplKHbhXXrow',
    'NID': '529=ZR8s33KS8Nft-P7rYdlIGVpuItIeCzt1G4Ft8wBfkyuq52r1trwP8ohKmszMWsMrc8YazukfBLgRDkKQn40cu2FU2N7tycxMfrgccNlgykSwjR9LhUHFihN_Sq0APpj-fJEjr6mpyGdxmhw674K5uAoGyAqkLTMYevCNKIiqpT3FUkvndDCMVoUFNvaJiGo7yRzjM-GWR7nvnulWMO33xYQaL_AtcbfzriRqntKsWEi7mL-tNw8oRrzM-tzbJO9mknXJAarwg8UHZ2dV85guHNgYGyCtYY9AE3othOGt72LpzP8f0KHZDV1FXs7KzemIvJjnlgIW2KfGpJ8DFrNeUA9G10zYmqHbRnKyQrZ__Ff6rvY0GFrt0U3CpzroKSggb79r4Ksa7YISXPyASsPhTfZC0pZQlXYoRAPAZ-_MWw56wKnIDRnvFNJ1myHOrNvhurnfxc3-MHJnFukHLtmfRGSKo50HOjWSf0nBlb3sRjNnq6OyUmZo-wW1T6ZvhWZhDbafiGRyWBAFZ1kuoRaZ_Tnus_n_qYpmU_vvEw-oTbHtPrQoThR6qP2TSBzDR19sd8U6ubn7tfix5OZybwo5Nx0P6P384Hf9YjsH7_QitHS5x33s0jlpjINb0iqGVAYUagfo2ODDw2IFWH9-s3Cym-E30j9TdJueSZ3H8pw-Wl3AaBBubY1eEtyLSN2nfic7Kb0UEmT95CmmTdiacb4x-sCzve_uqfW1lSLsathJDtjrvTBylCArlWviRi-JJ2pw6OJ6g5IpQ1zHclxUvzzMg0Sf',
    '__Secure-1PSIDTS': 'sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA',
    '__Secure-1PSIDRTS': 'sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA',
    '__Secure-3PSIDTS': 'sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA',
    '__Secure-3PSIDRTS': 'sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA',
    'SIDCC': 'AKEyXzWxh1XstGxZao3DjzXy8VdB9lZLQca-crJkHoMVSQs9bRsWwACllHCjNh0eQRPV6SrULvo',
    '__Secure-1PSIDCC': 'AKEyXzVpfaMhdn0wwtNHbkXdV2jgtLxUP8kRnTeER3lp9bPoIW3eXNW8YgDUxN5DhBlDjD5Nj6c',
    '__Secure-3PSIDCC': 'AKEyXzVTNgCUOha7kh4NH8a1Ij6BqlCII-ln7JEbgkD_IKZ72PyHwe9YO0hiK1zdMS3RFiVjwQ',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'downlink': '10',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'rtt': '50',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-form-factors': '"Desktop"',
    'sec-ch-ua-full-version': '"145.0.7632.110"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Google Chrome";v="145.0.7632.110", "Chromium";v="145.0.7632.110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-browser-channel': 'stable',
    'x-browser-copyright': 'Copyright 2026 Google LLC. All Rights reserved.',
    'x-browser-validation': 'oWQepDUHextb1hsYrtJDGvl4nAw=',
    'x-browser-year': '2026',
    'x-client-data': 'CJC2yQEIpbbJAQipncoBCP2VywEIkqHLAQiFoM0BCI2gzwEInKvPAQiNrM8BCNStzwEIxq/PAQjIr88BCLSwzwEI0rHPARi7qcoBGOyFzwEYn7DPAQ==',
    # 'cookie': '__Secure-BUCKET=CMAH; SEARCH_SAMESITE=CgQIl6AB; SID=g.a0006whg7TzGS0owvhFG6ERBR2SNFrUtz5JbVfppXV26BG48v0o7iAuT2m5o8vs7j_qa9CDi7QACgYKAQASARMSFQHGX2MiQ-sknxhLblORoKMM75EZnhoVAUF8yKoyP3kzO7tTNClVeNEOd4tr0076; __Secure-1PSID=g.a0006whg7TzGS0owvhFG6ERBR2SNFrUtz5JbVfppXV26BG48v0o7HPPRJyPZRT42ihgv24ZlOwACgYKAVQSARMSFQHGX2MiVvgOADSnQTQ26_-7amF4thoVAUF8yKreday_Ser23PCgngWSFnGa0076; __Secure-3PSID=g.a0006whg7TzGS0owvhFG6ERBR2SNFrUtz5JbVfppXV26BG48v0o75E9Qmbb_-nBZcsZbOwx9GAACgYKAXUSARMSFQHGX2Mi9utbrEXPLNowrrB3YmnEGxoVAUF8yKr8PCk43hcjZH32gUgFYsGL0076; HSID=AEe3bhLYTfLwfdnui; SSID=AFv6Qvqp-rGqJBUfS; APISID=aniM27_cQhrOhdBb/A_afpNR6XFzWHO9tO; SAPISID=BcH3B18EuFt5C0p4/Ad0Rj8yoqNFeVVqgW; __Secure-1PAPISID=BcH3B18EuFt5C0p4/Ad0Rj8yoqNFeVVqgW; __Secure-3PAPISID=BcH3B18EuFt5C0p4/Ad0Rj8yoqNFeVVqgW; __Secure-ENID=31.SE=iBKeL1NwrwFh9zQZRdY0vc0QOUXynfdKLQaIsMsf-9NrzQbCCmekD34aau51OrjdA6yan_5s1DGX0xNPeP_QmH5d42PseqgaPcooslTQgCQhkj_2N8rtbPWfhcOCHm3GMCGSUyrFIg9Y3b-zUovs3rnn160l18Ab7A5vl99Jpa9NsXy7jGAaox20ycRPXCorcWkI8RJBmPLZUESWCkMx1bexcMGj-JX_dMx3Z-S92lUFCs5_8G6TPsom0bD9ZxKsCKtP4QVslK3tRqb40FA3OwYUafxxH57BtjJkQ9fNcRsmXhQ1w1tZWhk1QAUFxJbbY7NX-2-GL9ZBXSI; AEC=AaJma5vuohRnoycKcyBfinvX_ww8ZcsH2OKlgYtC8FIKWwsplKHbhXXrow; NID=529=ZR8s33KS8Nft-P7rYdlIGVpuItIeCzt1G4Ft8wBfkyuq52r1trwP8ohKmszMWsMrc8YazukfBLgRDkKQn40cu2FU2N7tycxMfrgccNlgykSwjR9LhUHFihN_Sq0APpj-fJEjr6mpyGdxmhw674K5uAoGyAqkLTMYevCNKIiqpT3FUkvndDCMVoUFNvaJiGo7yRzjM-GWR7nvnulWMO33xYQaL_AtcbfzriRqntKsWEi7mL-tNw8oRrzM-tzbJO9mknXJAarwg8UHZ2dV85guHNgYGyCtYY9AE3othOGt72LpzP8f0KHZDV1FXs7KzemIvJjnlgIW2KfGpJ8DFrNeUA9G10zYmqHbRnKyQrZ__Ff6rvY0GFrt0U3CpzroKSggb79r4Ksa7YISXPyASsPhTfZC0pZQlXYoRAPAZ-_MWw56wKnIDRnvFNJ1myHOrNvhurnfxc3-MHJnFukHLtmfRGSKo50HOjWSf0nBlb3sRjNnq6OyUmZo-wW1T6ZvhWZhDbafiGRyWBAFZ1kuoRaZ_Tnus_n_qYpmU_vvEw-oTbHtPrQoThR6qP2TSBzDR19sd8U6ubn7tfix5OZybwo5Nx0P6P384Hf9YjsH7_QitHS5x33s0jlpjINb0iqGVAYUagfo2ODDw2IFWH9-s3Cym-E30j9TdJueSZ3H8pw-Wl3AaBBubY1eEtyLSN2nfic7Kb0UEmT95CmmTdiacb4x-sCzve_uqfW1lSLsathJDtjrvTBylCArlWviRi-JJ2pw6OJ6g5IpQ1zHclxUvzzMg0Sf; __Secure-1PSIDTS=sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA; __Secure-1PSIDRTS=sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA; __Secure-3PSIDTS=sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA; __Secure-3PSIDRTS=sidts-CjYBBj1CYlbWnPfSDb1Y2kJVFVlkWqr804Y5byAihFvh8aasQ9bGayrOBJupZ3k6rl8kaXvODJYQAA; SIDCC=AKEyXzWxh1XstGxZao3DjzXy8VdB9lZLQca-crJkHoMVSQs9bRsWwACllHCjNh0eQRPV6SrULvo; __Secure-1PSIDCC=AKEyXzVpfaMhdn0wwtNHbkXdV2jgtLxUP8kRnTeER3lp9bPoIW3eXNW8YgDUxN5DhBlDjD5Nj6c; __Secure-3PSIDCC=AKEyXzVTNgCUOha7kh4NH8a1Ij6BqlCII-ln7JEbgkD_IKZ72PyHwe9YO0hiK1zdMS3RFiVjwQ',
}

params = {
    'q': 'india',
    'sca_esv': 'ee81a51e8e25352b',
    'rlz': '1C1UEAD_enIN1180IN1180',
    'udm': '2',
    'biw': '1600',
    'bih': '250',
    'sxsrf': 'ANbL-n7WwlIuZk8n5pRtLUGgJlI-hJbUKg:1772027616182',
    'ei': '4P6eac3kCtP4seMPktfUsQM',
    'oq': '',
    'gs_lp': 'Egtnd3Mtd2l6LWltZyIAKgIIAzIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAjIKECMYJxjJAhjqAkjzQlD5BVjPD3ADeACQAQSYAeUBoAHbBqoBBTAuNS4xuAEByAEA-AEBmAIEoAKEAqgCCsICBxAjGCcYyQLCAgUQABiABJgDC4gGAZIHBTMuMC4xoAe2HbIHAzItMbgH7AHCBwUyLTMuMcgHGIAIAA',
    'sclient': 'gws-wiz-img',
}

response = requests.get('https://www.google.com/search',
                        params=params,
                        # cookies=cookies,
                        headers=headers
                        )


print(response.text)
print(response.status_code)