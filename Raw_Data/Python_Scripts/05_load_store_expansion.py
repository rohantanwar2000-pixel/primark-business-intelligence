import pandas as pd
import mysql.connector

data = [
    # 2019
    {"year": 2019, "country": "UK & Ireland", "region": "Europe", "stores_opened": 8, "stores_closed": 0, "total_stores": 189, "selling_space_sqft_m": 7.2},
    {"year": 2019, "country": "Spain", "region": "Europe", "stores_opened": 3, "stores_closed": 0, "total_stores": 50, "selling_space_sqft_m": 1.8},
    {"year": 2019, "country": "Germany", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 31, "selling_space_sqft_m": 1.1},
    {"year": 2019, "country": "USA", "region": "Americas", "stores_opened": 4, "stores_closed": 0, "total_stores": 13, "selling_space_sqft_m": 0.6},
    {"year": 2019, "country": "France", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 26, "selling_space_sqft_m": 0.9},
    {"year": 2019, "country": "Other Europe", "region": "Europe", "stores_opened": 5, "stores_closed": 0, "total_stores": 64, "selling_space_sqft_m": 2.1},
    # 2020
    {"year": 2020, "country": "UK & Ireland", "region": "Europe", "stores_opened": 3, "stores_closed": 0, "total_stores": 191, "selling_space_sqft_m": 7.3},
    {"year": 2020, "country": "Spain", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 52, "selling_space_sqft_m": 1.9},
    {"year": 2020, "country": "Germany", "region": "Europe", "stores_opened": 1, "stores_closed": 0, "total_stores": 32, "selling_space_sqft_m": 1.1},
    {"year": 2020, "country": "USA", "region": "Americas", "stores_opened": 3, "stores_closed": 0, "total_stores": 16, "selling_space_sqft_m": 0.7},
    {"year": 2020, "country": "France", "region": "Europe", "stores_opened": 1, "stores_closed": 0, "total_stores": 27, "selling_space_sqft_m": 0.9},
    {"year": 2020, "country": "Other Europe", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 66, "selling_space_sqft_m": 2.2},
    # 2021
    {"year": 2021, "country": "UK & Ireland", "region": "Europe", "stores_opened": 4, "stores_closed": 0, "total_stores": 193, "selling_space_sqft_m": 7.4},
    {"year": 2021, "country": "Spain", "region": "Europe", "stores_opened": 3, "stores_closed": 0, "total_stores": 55, "selling_space_sqft_m": 2.0},
    {"year": 2021, "country": "Germany", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 34, "selling_space_sqft_m": 1.2},
    {"year": 2021, "country": "USA", "region": "Americas", "stores_opened": 4, "stores_closed": 0, "total_stores": 20, "selling_space_sqft_m": 0.9},
    {"year": 2021, "country": "France", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 29, "selling_space_sqft_m": 1.0},
    {"year": 2021, "country": "Other Europe", "region": "Europe", "stores_opened": 3, "stores_closed": 0, "total_stores": 67, "selling_space_sqft_m": 2.3},
    # 2022
    {"year": 2022, "country": "UK & Ireland", "region": "Europe", "stores_opened": 4, "stores_closed": 0, "total_stores": 196, "selling_space_sqft_m": 7.5},
    {"year": 2022, "country": "Spain", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 57, "selling_space_sqft_m": 2.1},
    {"year": 2022, "country": "Germany", "region": "Europe", "stores_opened": 1, "stores_closed": 0, "total_stores": 35, "selling_space_sqft_m": 1.2},
    {"year": 2022, "country": "USA", "region": "Americas", "stores_opened": 4, "stores_closed": 0, "total_stores": 24, "selling_space_sqft_m": 1.1},
    {"year": 2022, "country": "France", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 31, "selling_space_sqft_m": 1.1},
    {"year": 2022, "country": "Other Europe", "region": "Europe", "stores_opened": 5, "stores_closed": 0, "total_stores": 65, "selling_space_sqft_m": 2.3},
    # 2023
    {"year": 2023, "country": "UK & Ireland", "region": "Europe", "stores_opened": 5, "stores_closed": 0, "total_stores": 199, "selling_space_sqft_m": 7.6},
    {"year": 2023, "country": "Spain", "region": "Europe", "stores_opened": 3, "stores_closed": 0, "total_stores": 60, "selling_space_sqft_m": 2.2},
    {"year": 2023, "country": "Germany", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 37, "selling_space_sqft_m": 1.3},
    {"year": 2023, "country": "USA", "region": "Americas", "stores_opened": 5, "stores_closed": 0, "total_stores": 29, "selling_space_sqft_m": 1.3},
    {"year": 2023, "country": "France", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 33, "selling_space_sqft_m": 1.2},
    {"year": 2023, "country": "Other Europe", "region": "Europe", "stores_opened": 4, "stores_closed": 0, "total_stores": 74, "selling_space_sqft_m": 2.5},
    # 2024
    {"year": 2024, "country": "UK & Ireland", "region": "Europe", "stores_opened": 4, "stores_closed": 0, "total_stores": 202, "selling_space_sqft_m": 7.7},
    {"year": 2024, "country": "Spain", "region": "Europe", "stores_opened": 3, "stores_closed": 0, "total_stores": 63, "selling_space_sqft_m": 2.3},
    {"year": 2024, "country": "Germany", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 39, "selling_space_sqft_m": 1.4},
    {"year": 2024, "country": "USA", "region": "Americas", "stores_opened": 6, "stores_closed": 0, "total_stores": 35, "selling_space_sqft_m": 1.6},
    {"year": 2024, "country": "France", "region": "Europe", "stores_opened": 2, "stores_closed": 0, "total_stores": 35, "selling_space_sqft_m": 1.3},
    {"year": 2024, "country": "Other Europe", "region": "Europe", "stores_opened": 5, "stores_closed": 0, "total_stores": 77, "selling_space_sqft_m": 2.5},
]

df = pd.DataFrame(data)

print("--- Primark Store Expansion Dataset ---")
print(df.to_string(index=False))

df.to_csv("/Users/rohantanwar/Downloads/Primark/Cleaned_Data/primark_store_expansion.csv", index=False)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan_123!!!",
    database="primark_project"
)
cursor = conn.cursor()
cursor.execute("DELETE FROM primark_store_expansion;")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO primark_store_expansion (
            year, country, region, stores_opened,
            stores_closed, total_stores, selling_space_sqft_m
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row["year"]),
        row["country"],
        row["region"],
        int(row["stores_opened"]),
        int(row["stores_closed"]),
        int(row["total_stores"]),
        float(row["selling_space_sqft_m"])
    ))

conn.commit()
cursor.close()
conn.close()

print("\nSuccessfully loaded into MySQL!")
print(f"Total rows inserted: {len(df)}")