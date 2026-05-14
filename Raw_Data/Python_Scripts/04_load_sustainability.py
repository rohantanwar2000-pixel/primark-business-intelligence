import pandas as pd
import os
import mysql.connector

data = [
    {
        "reporting_year": 2022,
        "sustainable_materials_pct": 45.0,
        "recycled_fibres_pct": 25.0,
        "ghg_reduction_vs_2019_pct": 3.0,
        "scope1_2_reduction_pct": 22.0,
        "supplier_audits_total": 800,
        "workers_reached_programmes": 160000,
        "cotton_project_farmers": 85000
    },
    {
        "reporting_year": 2023,
        "sustainable_materials_pct": 66.0,
        "recycled_fibres_pct": 32.0,
        "ghg_reduction_vs_2019_pct": 4.2,
        "scope1_2_reduction_pct": 51.0,
        "supplier_audits_total": 850,
        "workers_reached_programmes": 190000,
        "cotton_project_farmers": 90000
    },
    {
        "reporting_year": 2024,
        "sustainable_materials_pct": 74.0,
        "recycled_fibres_pct": 39.0,
        "ghg_reduction_vs_2019_pct": 5.7,
        "scope1_2_reduction_pct": 71.0,
        "supplier_audits_total": 900,
        "workers_reached_programmes": 220000,
        "cotton_project_farmers": 95000
    }
]

df = pd.DataFrame(data)

print("--- Primark Sustainability Dataset ---")
print(df.to_string(index=False))

os.makedirs("/Users/rohantanwar/Downloads/Primark/Cleaned_Data", exist_ok=True)
df.to_csv("/Users/rohantanwar/Downloads/Primark/Cleaned_Data/primark_sustainability.csv", index=False)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan_123!!!",
    database="primark_project"
)
cursor = conn.cursor()
cursor.execute("DELETE FROM primark_sustainability;")

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO primark_sustainability (
            reporting_year, sustainable_materials_pct, recycled_fibres_pct,
            ghg_reduction_vs_2019_pct, scope1_2_reduction_pct,
            supplier_audits_total, workers_reached_programmes,
            cotton_project_farmers
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("\nSuccessfully loaded into MySQL!")
print(f"Total rows inserted: {len(df)}")