import pandas as pd
import mysql.connector

df = pd.read_csv("/Users/rohantanwar/Downloads/Primark/Cleaned_Data/primark_financials.csv")

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan_123!!!",
    database="primark_project"
)

cursor = conn.cursor()

cursor.execute("DELETE FROM primark_financials;")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO primark_financials (
            year, revenue_gbp_m, operating_profit_gbp_m,
            operating_margin_pct, store_count, employee_count,
            like_for_like_growth_pct, selling_space_sqft_m
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        int(row["year"]),
        float(row["revenue_gbp_m"]),
        float(row["operating_profit_gbp_m"]),
        float(row["operating_margin_pct"]),
        int(row["store_count"]),
        int(row["employee_count"]),
        float(row["like_for_like_growth_pct"]),
        float(row["selling_space_sqft_m"])
    ))

conn.commit()
cursor.close()
conn.close()

print("Successfully loaded into MySQL!")
print(f"Total rows inserted: {len(df)}")