from pathlib import Path

import pandas as pd

app_dir = Path(__file__).parent.parent
# tips = pd.read_csv(app_dir / "tips.csv")
assets_dir = app_dir / "assets"

country_list = ['Cambodia', 'Bangladesh', 'India', 'Indonesia', 'China', 'Africa']