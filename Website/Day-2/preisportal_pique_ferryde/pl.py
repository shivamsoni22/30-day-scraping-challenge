import os
import json
import requests
import pandas as pd
from datetime import datetime

platform_name = "preisportal_pique_ferryde"
type_name = "pl"

output_base = r"D:\30-day-scraping-challenge\output file"
pages_base = r"D:\30-day-scraping-challenge\pagesave"

output_path = os.path.join(output_base, platform_name, type_name)
pages_path = os.path.join(pages_base, platform_name, type_name)

os.makedirs(output_path, exist_ok=True)
os.makedirs(pages_path, exist_ok=True)

url = "https://preisportal.pique-ferry.de/api/query"

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://preisportal.pique-ferry.de',
    'priority': 'u=1, i',
    'referer': 'https://preisportal.pique-ferry.de/?locale=en',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Google Chrome";v="145", "Chromium";v="145"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'eyJpdiI6Ikt4NEVtMHpEZTNXZUxTbkhKSlNtTmc9PSIsInZhbHVlIjoibjBIempva25KVUVibVJNY1B3eTFVRjNMZ1J0T2U0VitIZldZd05VSDdLYUNETktaYk8wVGdlaVhqZFlQRmJHWUtnRG1PSnJxS0FpcUlWRThPTWdBVGRTdFJGbnlKUW91Z0dMNE4wYVc3KzlWem8wVVA0dDFFYXVHMUFvYzBacy8iLCJtYWMiOiIzOTE4NGQ3M2M5MzIwZDgwMjBlOGI2OTI1M2YxNjY0YmJjNDkzZGFiNWJkNTY3YzdlYWY5NWVlNmJjNDViNDJlIiwidGFnIjoiIn0=',
    'cookie': '_ga=GA1.1.1778200087.1771476839; _ga_EH638XP6NL=GS2.1.s1771476838$o1$g1$t1771477416$j18$l0$h0; XSRF-TOKEN=eyJpdiI6Ikt4NEVtMHpEZTNXZUxTbkhKSlNtTmc9PSIsInZhbHVlIjoibjBIempva25KVUVibVJNY1B3eTFVRjNMZ1J0T2U0VitIZldZd05VSDdLYUNETktaYk8wVGdlaVhqZFlQRmJHWUtnRG1PSnJxS0FpcUlWRThPTWdBVGRTdFJGbnlKUW91Z0dMNE4wYVc3KzlWem8wVVA0dDFFYXVHMUFvYzBacy8iLCJtYWMiOiIzOTE4NGQ3M2M5MzIwZDgwMjBlOGI2OTI1M2YxNjY0YmJjNDkzZGFiNWJkNTY3YzdlYWY5NWVlNmJjNDViNDJlIiwidGFnIjoiIn0%3D; preisportal_session=eyJpdiI6InQ2QXJycGlXZks2bWVxWFBNTWxab1E9PSIsInZhbHVlIjoiaTB2dlp6bmI4WFlLNmtkQ2xLU2x3eXpyaU5JczlTZkcvT3JvL0xab2F5TFZ4dHNLRCtURmdjeVJ0Z1VTZzF0NndSbWVlcWpWaXQ4SkNJSlZhdVZ2VWYxQk9IQ0ZSaFBpYnFhdGY3STJDTXgwSWZmWjlVMVVaODdwalF4WlpYMk4iLCJtYWMiOiI0ZDVhOWJjMWVmMjNkOWZiNDkxZjk1N2VjODNlZmE3NDEzMmQyYzBiYjFhZjcxOWFjNTdmNWMwNTZkMDMxNmQ1IiwidGFnIjoiIn0%3D',
}

json_data = {
    'harbour_from_id': 235,
    'harbour_to_id': 234,
    'date': '2026-02-17T18:30:00.000Z',
    'length': '18',
    'powerPlug': False,
    'secondDriver': False,
    'empty': False,
}
response = requests.post(url, headers=headers, json=json_data)

print("Status Code:", response.status_code)

if response.status_code != 200:
    print(response.text[:500])
    exit()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

html_file = os.path.join(pages_path, f"{platform_name}_{type_name}_{timestamp}.html")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(response.text)

try:
    data = response.json()
except:
    print("Invalid JSON")
    print(response.text[:1000])
    exit()

if isinstance(data, str):
    data = json.loads(data)

if isinstance(data, dict):
    for key, value in data.items():
        if isinstance(value, list):
            data = value
            break

if not isinstance(data, list):
    print("No list found in JSON structure")
    print(json.dumps(data, indent=2)[:1000])
    exit()
all_rows = []

for trip_index, trip in enumerate(data):

    if not isinstance(trip, dict):
        continue

    main_departure = trip.get("departure")
    main_travel_time = trip.get("travelTime")
    price_list = trip.get("priceList", [])

    if not isinstance(price_list, list):
        continue

    for group_index, group in enumerate(price_list):

        if not isinstance(group, list):
            continue

        for price_index, item in enumerate(group):

            if not isinstance(item, dict):
                continue

            row = {
                "trip_index": trip_index,
                "main_departure": main_departure,
                "main_travel_time": main_travel_time,
                "price_group_index": group_index,
                "price_index": price_index,
                "price": item.get("price"),
                "info": item.get("info"),
                "infoIndex": item.get("infoIndex"),
                "date": item.get("date"),
                "carrier": item.get("carrier"),
                "dayOfWeek": item.get("dayOfWeek"),
                "travelTime": item.get("travelTime"),
                "departure": item.get("departure"),
                "departureId": item.get("departureId"),
                "onlineBooking": item.get("onlineBooking")
            }

            all_rows.append(row)

if all_rows:
    df = pd.DataFrame(all_rows)
    excel_file = os.path.join(output_path, f"{platform_name}_{type_name}_{timestamp}.xlsx")
    df.to_excel(excel_file, index=False)
    print("Data Saved:", excel_file)
else:
    print("No Data Found")