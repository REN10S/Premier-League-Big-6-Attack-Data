import pandas as pd

url = "https://fbref.com/en/comps/9/2018-2019/stats/2018-2019-Premier-League-Stats"

tables = pd.read_html(url)
print(f"Number of tables found: {len(tables)}")

for i, table in enumerate(tables):
    print(f"\nTable {i}")
    print(table.head())