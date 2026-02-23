from lxml import html
import pandas as pd
from curl_cffi import requests
url = "https://www.hotelchains.com/united-kingdom/"
cookies = {
    'cf_clearance': 'PEmP66A2KyMU6mktfDpHowFr_wvF_yN44oGIlL2_UiM-1771827595-1.2.1.1-LS3lwU8Ex7JzGxYHQOTkSPBiovI8dBU4ghMjpbEl73hbTAz_PTQVSpiTI4yFJZqtSV5WaZkQ50qJ4.va9l2e8dHIGI.XWXY0eRK3I9SSadmqgKlRBFKxcU1F6zAZyCTEXUr8uBASRc9yGB3UCcycxXlQS7oMN7E.Itb_WjtguSpuqPt.CD3d7AKr4p59iwH752CHdBXwPxTt_noL.Oa9XnV4fFYs3QriZ1L.sYyWoa0aRIkcKGzKXhNFZsMWtZmO',
    '_ga_796DWW014E': 'GS2.1.s1771827596$o1$g0$t1771827596$j60$l0$h0',
    '_ga': 'GA1.1.925457895.1771827596',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'if-modified-since': 'Thu, 12 Feb 2026 10:00:18 GMT',
    'origin': 'https://www.hotelchains.com',
    'priority': 'u=0, i',
    'referer': 'https://www.hotelchains.com/united-kingdom/?__cf_chl_tk=VM2_c5Lf9bdIajsQFSjHmCv9gYXubYm7HcUr8zxoxSk-1771827576-1.0.1.1-aoc8PW2U0bvDYMvyuas5RMUec_f73OG.Cwc5sgwj4cA',
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
    # 'cookie': 'cf_clearance=PEmP66A2KyMU6mktfDpHowFr_wvF_yN44oGIlL2_UiM-1771827595-1.2.1.1-LS3lwU8Ex7JzGxYHQOTkSPBiovI8dBU4ghMjpbEl73hbTAz_PTQVSpiTI4yFJZqtSV5WaZkQ50qJ4.va9l2e8dHIGI.XWXY0eRK3I9SSadmqgKlRBFKxcU1F6zAZyCTEXUr8uBASRc9yGB3UCcycxXlQS7oMN7E.Itb_WjtguSpuqPt.CD3d7AKr4p59iwH752CHdBXwPxTt_noL.Oa9XnV4fFYs3QriZ1L.sYyWoa0aRIkcKGzKXhNFZsMWtZmO; _ga_796DWW014E=GS2.1.s1771827596$o1$g0$t1771827596$j60$l0$h0; _ga=GA1.1.925457895.1771827596',
}
data_payload = {}
# data = {
#     '1322aaf2abd0cdb0239d6efd535d9c5bade95a74fd615dc0b393a92ba14b1d86': 'FKurIOFOG4wRTfJVIbLLumWKn5kyjhiz4LV6jMvUKb4-1771827576-1.2.1.1-R1gt_mHZFOIe4ERi3s5IujWPVkiHC1.NCoVP8P94FOsTCLsJwn7lFFUk42Ao3boOyxzmQULkzGPnHjjpV7_zJ2DeSjuDxpydWcHvxk.RnBuGUCAUgwFYxmhdUlKgLGVLoWPq3p8_GNXwFJYkygiqwjNqsfgFuyuRitNWMnFz4_wZnFgoyarOd2AYl7HW.HQry5EUjZSR8pmfuLF7Fp1M_FtgXbGh2D3WqXK3mWPxKfiZFgyb__OemU2PH55J2brIIu3WKQwbK6QvOAahs38CiP0xRcz3ZhkC7BKvt7EiqpVQ45Oznr3fkzsyilE4WgG7oLn54SOgcCTBFK7GqoBWlFmLOpzYHgpuclaA7YIaQ82_mH5YNYgqay1WezC9V5IXughT1esLt4ptGVroSfNH1gY6jmNSZ3cifX.0fbxD5aNuszskWknzhr.39T.JJQ5vbdb6EU.M1Mig5PXNYRW.qZ8oi0ls2hq5F8g.dszvAe0EtkGh1GUavpNElj3VpmV2lpJD9gUKu_zc7r8bJNaAdDtQUP92Z3CPcQgi315G4rW_TSNflxRGXuRIrGt.FGvPKVwQPsqcetYPIVrq5GB9jMVCYb0R8gLb5VWGWr1rChkMZC6cJAqWh2rUUODdY.wOQrem7sm2TXAkAym1auaxe_draeTCah_cWOx4QzpmBN3HkPZz2ai.8Pnon._zguvFxq1WSZbZEeCewXdSpzzhWzw5vK2jO8h0SbX9scQuXRh_hZPRciEJxSfSBZrYukbbJyuFzeMvkjbS30XuJcQvZu61fTKDnAw2LFBJ.ckBwli4frIRIOn_h4lnO96_lfGvXgydBk3_3gy9edMJJnVdAJLEdYJFjG_dh0JZZaokUHZewxJ7gvLQIipHvhiKNeUw6Puevpmqnf7WltsZuvQwwLNeX_6rllFeOfikxLBV5gDY5PNRLzbZ.QJyfwGj7DDNkW7v6z9XH4dTQ2NZp6aX0i1XowiNEo9flBUBRsc9mFmzdtKuo7_Rf5NosIHwp8GuQSJgkdwAj.KKm0M.Mi1AhZ0YCdmc0LRQWhoRl74xmrI',
#     '85f42331ae184559d0579a808d9f576151b2321e5bce1d793a858f73059aede7': 'uDImdCo3IpxvQERllSsmGi5ZOdQehHhiUHLbHIhfhoE-1771827576-1.2.1.1-geSmpwFmdlXcR9Rl4xrNR9GHhE.9Qre12GqUst2fp1LU17bxabvY4JuyiKCJEsCTyrbKt9MRDIJIf2F11yGplPzukDifA37wz1bGa2UFh2mM.zGAdAq9baJiKojM6AMv0LlsN5wAzdU0wJL942z5c6dLhQ9yfXj9zthL16SP8V316I2ZzE6OT2amDPfU0qB_DoWRG8SHa3ouZtuRApph6AL5wNnBE0qlPffIhfWAcL5r5SxkC.4bxLZjZ4vTfOyiHGEPDynpmpMc0hsatyGTccm74Y7OMx84DOEJfOuRlCYcc1hP151hcCE4vPGPsdxQDUOxkP8IX8Ptbry3rFwUgi.wSTStK169_G9Wncxb52FEZVpQxbWu1.3Hen0yje76Ci4F1iuZRIzXt9MLb7AOCOZlWd4iiWFq.3EpZnHXLLaEMHyY2tasVCACQyL1bP3urm9qWiBb_W_DjNBD5uC4hV_.v_GP7c4LNyDKTUSWkuL.2RxsvwUJAYuSqS2RusDy29ewNMIFtesGA5CzMFYPuoiQaNz7rJ7GYs5rOGI_Jf7de.g_FuWltkjmkf9qjW1.q51dFGyVYQVModJx6A_pNPLRdUQBzkZ7uSeI5aLMo2dGLol6.kx4qzrlTv9JTtIP6uyj26gf3aXJSk1EerL7wVSnIUTRrD6j3C8xDQR3S_DOw78kaWDVuPdM9lMpH17msg3gxSKq0HYNLQqE2h5apOoLq4Q8ncFJd0KCBfIQBK2Rx0FUsJoiJH5b55ppwAGNAMCWXGs4kA4D6dYWIxTWOuQjHNPNz9aDaie4uJV_T6VYwDUyDbrnrztRGNoopADg0s3EL6HaRAfiWSMDwl_nTGANC1VDNp8OGhKF5QhqiULK.Z3YDvS0mFg6Hi_PR6mOTG3bozmCG1BnAnyLkq12jTKrv9IOxvPlBR7oD88xLwRgHqRqU1hs2LPdHMcwK1mTKtjsKj190Dr.LwKYmGAPDVmmS9bcOSKcQ6IxNg3rK59JhmcuYn8zl0KK5vwi04xb5bDYsxQHuoZJlMjqka.AFEPwMJ1Bju5zF9QFZSQOkKLUXy48yKn9EEnDk8PftLf_gcm7ZmZt7LBDvoZEsT7iBFodpMzln8Bwdx_VJyKizmlt9UUEwuZnWJE3pROWa4Jt8MVCVl9cX6fXK4YH1HIaEzEcEe6hn_TR6RNK6GWaVwM3Mc5HV.RqUB9jONavGFOuGS0hByD01c5VeorASpgGvcwQFwqK3d3UndrAQ4k9zlyXSpXu4M7hXtE9w8tJUysB5Kca8FlwZUHyNXT1REkw83SRuImKwrOeU.BEw7whykgDKOfdc6gC23Z_vBJ7saaIGrbTtu6GP4sR3slhgOjklVDSKIW3PRE55GOKB0BESLzgMqkFvJRYOLD82U6v34f0907GHiKVK8tOYE86dOywWxQ.2a41SiFO41VYmhxIymeLSvPhaynIEN9g34GZCAgPSE_QAUq113lLj_Ld9k2NtLiPHQJFhrd_lXDBSqUrEuqIkFi7lcAnpuoC0hHlDXzsR29G_zhUcRumlavqNdKwW77aKeir.VMmJb6x14.rP_A73Y00.n.z1oOHXn8JJV8UwASQxqKe2XqOZqZ815.Di81evZcx.gq6ZGLx9V3Bh8nUg0rl8_YQqc44HohLNXAm7kPuDveNmJRg_.cWlV0kkAnXvsT9UDa8lgsHWkx9gAOVzgUdV8lfVPpuoDs_DdaOov0uKsF3uYB3GbbwGrquYwBFL_J7n5Vq.a_E.6r0bcPmBtpDatFOMQw8xwzyB804JNKNbdmKTEIF9k8hGRpeBg803DNRkUkoEsyxNYwPvEyLHWZy5yckN8aDZdffGW2nizPwTu9yR.6O12kdc5QzoDQkdHgTVwNYVpa7pJzbX9Dq8Ql5CBnYa0lu26tJvEZZf6S7pJYJv8H_3zQhEZ2bmuMXUm8RwTY_Nf.isLZ_.1L4wpaDBQfmDvaXnVb_5QoHWWXjswP7wUMX7fPs00LlbxD656rHbxnBIQ.wosftNBlClmcOwyHzZl3BenAy42nwS1R0tcWyNUi.BtaaBGLmOn1wrxXvpHHas1u5ZMbFuhQ1Tbu40tZ9H6vMoHjcDnVC8exv1fAcMNfi5u_xn_YHOQ.AV9tjoPBM52D8p.3B_Tw16ZwAKTs6hG2Qs2UtXkI7JUMcmex2E1dIgT2ux5V9xYBI2JPsEXCiGzcwkvGA0Gp0SjXG6r0LQRLnBv2AzZRbm6awVdDcl34CQCSzayleeYrGU3EONMIjQ_GQCXeMo8EinZBiyP1s7dTwasC_EC2NyNAVNgGRa5K9rXxlRduywIEH.52UyMU0xw1tW83nCpwW.CYLrX6w6wWSQsXDIV4eRr.1l2p6T5COvBiqooWyJi07tQP26S_WCpwsHUBZaEotcgEwVT.ehX066lYrjEQIGdWjJBkwqIErAlQ8l0Hk0OPuW35Z1BOnjuog7gL9cdJ0FERgmAhUY1IvpP_VC9TZHWjJ8qYKO.xEPeXZRsl6GzXIidMtJWHNwTWO5DWK2j4iNK6aY1Xv4ualyw03.t1i7bV5LpZzDzIEVc4JSds_8jQmlIe8tLhd0QFdhoCinlhzYcFUNPzk7rvqPd5B2_zg',
#     '6bf2291582950a75189c5d185122c6bffed2afc4394f805fd7a03f5e7a18dbe8': '3wXuCnNxvHuqnb5Zjy5p6Lt.uSLu2pn.WJRALRdQEYI-1771827588-1.0.1.1-UFx69ar1pVJbF4nLf0Li83R08KYUIlqk3F0qHQChWJGABmcMZmHhVaR_NpUoctWwM9RA1Gq811jTbowQLxnsT7VMYkWbsIH_vFb9pl6AvkAsVyLAzZWRo7VR4FcY9LIQNST1uCNtkDcYKGpg7Vau30e53Ed.FxDDt69KXm305I.Yz7CpEGWVPhh43d8vSNbc',
# }

response = requests.get(url,
                        # cookies=cookies,
                        headers=headers, data=data_payload,
                        impersonate ='chrome120'
                        )

print("Status Code:", response.status_code)

if response.status_code != 200:
    print("Blocked by Cloudflare")
    exit()

tree = html.fromstring(response.content)

names = tree.xpath('//div[@class="fw-bold text-uppercase text-truncate"]/text()')
images = tree.xpath('//img[@class="img-fluid"]/@src')
urls = tree.xpath('//a[@class="text-decoration-none text-dark d-block"]/@href')

print("Names Found:", len(names))
print("Images Found:", len(images))
print("URLs Found:", len(urls))

records = []

for name, image, link in zip(names, images, urls):
    records.append({
        "Hotel Name": name.strip(),
        "Image URL": "https://www.hotelchains.com"+image,
        "Hotel URL": "https://www.hotelchains.com" + link if link.startswith("/") else link
    })

df = pd.DataFrame(records)

df.to_excel(r"D:\30-day-scraping-challenge\output file\hotelchains_uk\hotelchains_uk.xlsx", index=False)

print("Excel file saved successfully")