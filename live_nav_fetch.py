import requests
import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

SCHEMES = {
"HDFC_Top_100_Direct": 125497,
"SBI_Bluechip": 119551,
"ICICI_Bluechip": 120503,
"Nippon_Large_Cap": 118632,
"Axis_Bluechip": 119092,
"Kotak_Bluechip": 120841
}

for fund_name, scheme_code in SCHEMES.items():

```
url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)
response.raise_for_status()

data = response.json()

nav_df = pd.DataFrame(data["data"])

output_file = RAW_DIR / f"{fund_name}.csv"

nav_df.to_csv(output_file, index=False)

print(
    f"{fund_name} saved -> "
    f"{len(nav_df)} records"
)
```

print("NAV download complete.")
