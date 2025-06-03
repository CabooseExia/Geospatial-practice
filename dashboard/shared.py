from pathlib import Path

import pandas as pd
import os

app_dir = Path(__file__).parent.parent
# tips = pd.read_csv(app_dir / "tips.csv")
assets_dir = app_dir / "assets"

# country_list = ['Cambodia', 'Bangladesh', 'India', 'Indonesia', 'China', 'Africa']
# test = [f for f in os.listdir(assets_dir) if f.endswith(".html")]
# with open(assets_dir / "Cambodia_map.html", "r") as file:
#     test = file.read()
# print(test)

country_list = sorted(
    [f.stem for f in assets_dir.glob("*.html")]
)