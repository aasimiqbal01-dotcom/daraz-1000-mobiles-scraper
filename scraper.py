import requests
import csv
import time

headers = {"User-Agent": "Mozilla/5.0"}

all_mobiles = []
for page in range(1, 26):
    url = f"https://www.daraz.pk/catalog/?ajax=true&q=mobile&page={page}"
    data = requests.get(url, headers=headers).json()
    for item in data['mods']['listItems']:
        all_mobiles.append([
            item.get('name'),
            item.get('price'),
            item.get('originalPrice'),
            item.get('ratingScore'),
            item.get('review')
        ])
    time.sleep(2)

with open("daraz_1000_mobiles.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Name","Price","Old_Price","Rating","Reviews"])
    w.writerows(all_mobiles)

print(f"DONE! Total {len(all_mobiles)}")
