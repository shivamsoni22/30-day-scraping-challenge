import asyncio
import json
from playwright.async_api import async_playwright
import os
import random
import requests
# from configs import sqlDatabase
from datetime import datetime
import base64

today_date = datetime.today().strftime("%d_%m_%Y")
ids_path = fr'D:\hrithik\pagesave\didifood\{today_date}'
os.makedirs(ids_path, exist_ok=True)
main_list = []
old_length = 0
_count = 0

time_out = 25
page_save_count = 60


DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1399316794518278277/UECsRqVYFlE7SMGrmbAYzPvlR6oiDXXsSiVB4vP9dY57lnsWT_JLp8U7AQGTO70ZazLB'

sql_obj = sqlDatabase()
conn = sql_obj.create_connection()
db_name = "didi_food"
sql_obj.create_database(conn, db_name)
table_name = "didi_links_oct_2025_p1"
system = '(165_sb_c1) | '

def send_discord_message(message):
    data = {
        "content": message,
        "username": "YoloBot"
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data)
        if response.status_code != 204:
            print(f"Failed to send Discord notification: {response.status_code}")
    except Exception as e:
        print(f"Error sending Discord notification: {e}")

async def save_intercepted_data(res_id, data):
    global main_list, _count
    file_name = os.path.join(ids_path, f'{res_id}.html')
    new_length = len(os.listdir(ids_path))
    # send_discord_message(f'{system}{new_length} | {len(main_list)} | {_count}')
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(data)
        main_list.append(file_name)
        _count = 0
    query = f"""UPDATE {table_name} SET status = 'done' WHERE store_id = '{res_id}'"""
    sql_obj.update_data(conn, db_name, query)
    print(f"Saved page to: {file_name}")

async def intercept_response(response):
    global old_length, _count
    if "https://c.didi-food.com/shop/index" in response.url:
        new_length = len(os.listdir(ids_path))
        if old_length == new_length:
            _count += 1
            if _count >= 4:
                send_discord_message(f'{system} program stop...')
                send_discord_message(f'{system} page save count = {new_length} & stopped at {_count}')
                asyncio.get_running_loop().stop()
                os._exit(1)
            else:
                # send_discord_message(f'{system} {_count} data not scraped...')
                pass
        old_length = new_length
        if response.status not in [200]:
            return
        try:
            await response.finished()
            data = await response.text()
            json_d = json.loads(data)
            shopId = json_d['data']['shopInfo']['shopId']
            print(f"[Success] Shop ID: {shopId}")
            await save_intercepted_data(shopId, data)
        except Exception as e:
            pass

async def main():
    global main_list, _count, old_length

    query = f"""SELECT store_id 
            FROM `didi_links_oct_2025_p1` 
            WHERE `status` = 'pending' 
            ORDER BY id 
            LIMIT 1994 OFFSET 0;"""

    res_ids = sql_obj.fetch_data(conn, db_name, query)
    res_ids = [row[0] for row in res_ids]
    random.shuffle(res_ids)
    # res_ids = ['5764607530614128901']

    private_key = 'P2NoYW5uZWw9MTk='
    decoded_bytes = base64.b64decode(private_key.encode("utf-8"))
    decoded_key = decoded_bytes.decode("utf-8")

    async with async_playwright() as p:
        browser1 = await p.chromium.launch(
            headless=False,
            args = ["--start-maximized"]
        )

        for pos, ids in enumerate(res_ids):
            url = f'https://www.didi-food.com/es-MX/food/store/{ids}/{decoded_key}'
            file_name = os.path.join(ids_path, f'{ids}.html')
            file_exists = os.path.exists(file_name)
            print(f"\n[Loading] Store ID: {ids}")

            if file_exists:
                print(f'This id = {ids} already scraped', '\n')
                continue

            context = await browser1.new_context(no_viewport=True)
            # Page Create Without new_context()
            page1 = await context.new_page()

            page1.on("response", lambda r: asyncio.create_task(intercept_response(r)))

            response_event = asyncio.Event()
            await page1.goto(url, wait_until="domcontentloaded")

            try:
                await asyncio.wait_for(response_event.wait(), timeout=time_out)
            except asyncio.TimeoutError:
                pass

            try:
                await page1.close()
            except:
                pass

            new_length = len(os.listdir(ids_path))
            print(new_length, _count)

            if len(main_list) >= page_save_count:
                new_length = len(os.listdir(ids_path))
                send_discord_message(f'{system} program successfully stop...')
                send_discord_message(f'{system} page save count = {new_length} & stopped at {_count}')
                exit()
        print('\n')

send_discord_message(f'{system} program start...')
asyncio.run(main())