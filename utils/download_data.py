import os
import json

import requests


google_sheet_code = "1S35maYwCal1Be963wAQMPfn0VpwGKl1SmuasQnlO2Mg"
sheet_page_number = 1

while True:
    resp = requests.get(
        f"https://spreadsheets.google.com/feeds/cells/{google_sheet_code}/{sheet_page_number}/public/full?alt=json"
    )
    if resp.status_code != requests.codes.ok:
        break
    data = resp.json()
    title = data["feed"]["title"]["$t"]
    print(title)
    if title == "Sector-based Summary":
        entries = [x["gs$cell"] for x in data["feed"]["entry"]]
        [x.pop("inputValue") for x in entries]
        with open(f"./assets/{title}.json", "w") as f:
            json.dump(entries, f)
        break
    sheet_page_number += 1
