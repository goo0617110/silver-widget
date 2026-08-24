import json
import urllib.request
from datetime import datetime, timezone, timedelta

def get_price(symbol):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())

    return data["chart"]["result"][0]["meta"]["regularMarketPrice"]

silver = get_price("SI=F")
usd_jpy = get_price("USDJPY=X")

yen_per_gram = (silver / 31.1034768) * usd_jpy
total_648g = yen_per_gram * 648

jst = timezone(timedelta(hours=9))

result = {
    "silver_usd_oz": silver,
    "usd_jpy": usd_jpy,
    "yen_per_gram": round(yen_per_gram, 2),
    "total_648g": round(total_648g),
    "updated": datetime.now(jst).strftime("%Y-%m-%d %H:%M")
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(result)