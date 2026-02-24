import os
import json
import requests
from datetime import datetime

WEBSITE_NAME = "tacomascrew"
BASE_DIR = r"D:\30-day-scraping-challenge"

PAGE_SAVE_DIR = os.path.join(BASE_DIR, "pagesave", WEBSITE_NAME, "pl")
OUTPUT_DIR = os.path.join(BASE_DIR, "output file", WEBSITE_NAME)

os.makedirs(PAGE_SAVE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

API_URL = "https://www.tacomascrew.com/api/v1/catalogpages"

params = {
    "path": "/Catalog/fasteners/bolts"
}

response = requests.get(API_URL, params=params)

if response.status_code != 200:
    raise Exception(f"API Failed: {response.status_code}")

data = response.json()

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
page_save_file = os.path.join(PAGE_SAVE_DIR, f"bolts_{timestamp}.json")

with open(page_save_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

with open(page_save_file, "r", encoding="utf-8") as f:
    saved_data = json.load(f)

subcategories = []

subcats = saved_data.get("category", {}).get("subCategories", [])

for sub in subcats:
    sub_id = sub.get("id")
    sub_name = sub.get("name")
    url_segment = sub.get("urlSegment")

    full_url = f"https://www.tacomascrew.com/Catalog/fasteners/bolts/{url_segment}"

    subcategories.append({
        "id": sub_id,
        "name": sub_name,
        "url": full_url
    })

output_file = os.path.join(OUTPUT_DIR, "subcategories.json")

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(subcategories, f, indent=4)

for sub in subcategories:
    sub_path = f"/Catalog/fasteners/bolts/{sub['url'].split('/')[-1]}"

    params = {
        "path": sub_path
    }

    res = requests.get(API_URL, params=params)

    if res.status_code == 200:
        sub_data = res.json()

        file_name = sub["name"].replace(" ", "_") + ".json"
        sub_file_path = os.path.join(PAGE_SAVE_DIR, file_name)

        with open(sub_file_path, "w", encoding="utf-8") as f:
            json.dump(sub_data, f, indent=4)
    else:
        continue