import pandas as pd
import os
import mysql.connector

gender_pay_folder = "/Users/rohantanwar/Downloads/Primark/Raw_Data/Gender_Pay"

all_files = [f for f in os.listdir(gender_pay_folder) if f.endswith(".csv")]

dfs = []
for file in all_files:
    filepath = os.path.join(gender_pay_folder, file)
    df = pd.read_csv(filepath)
    year_str = file.replace("UK Gender Pay Gap Data - ", "").replace(".csv", "").strip()
    df["reporting_year"] = int(year_str.split(" to ")[0])
    dfs.append(df)

combined = pd.concat(dfs, ignore_index=True)

primark = combined[combined["EmployerName"].str.contains("Primark", case=False, na=False)]

print(f"Primark rows found: {len(primark)}")
print(primark[["EmployerName", "reporting_year", "DiffMeanHourlyPercent", "DiffMedianHourlyPercent"]].to_string())

primark_clean = primark[[
    "reporting_year",
    "DiffMeanHourlyPercent",
    "DiffMedianHourlyPercent",
    "DiffMeanBonusPercent",
    "DiffMedianBonusPercent",
    "FemaleLowerQuartile",
    "FemaleLowerMiddleQuartile",
    "FemaleUpperMiddleQuartile",
    "FemaleTopQuartile",
    "MaleBonusPercent",
    "FemaleBonusPercent"
]].copy()

primark_clean.columns = [
    "reporting_year",
    "mean_hourly_gap_pct",
    "median_hourly_gap_pct",
    "mean_bonus_gap_pct",
    "median_bonus_gap_pct",
    "pct_female_lower_quartile",
    "pct_female_lower_mid_quartile",
    "pct_female_upper_mid_quartile",
    "pct_female_upper_quartile",
    "pct_receiving_bonus_male",
    "pct_receiving_bonus_female"
]

primark_clean = primark_clean.sort_values("reporting_year").reset_index(drop=True)

print("\n--- Primark Gender Pay Dataset ---")
print(primark_clean.to_string(index=False))

os.makedirs("/Users/rohantanwar/Downloads/Primark/Cleaned_Data", exist_ok=True)
primark_clean.to_csv("/Users/rohantanwar/Downloads/Primark/Cleaned_Data/primark_gender_pay.csv", index=False)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan_123!!!",
    database="primark_project"
)
cursor = conn.cursor()
cursor.execute("DELETE FROM primark_gender_pay;")

for _, row in primark_clean.iterrows():
    cursor.execute("""
        INSERT INTO primark_gender_pay (
            reporting_year, mean_hourly_gap_pct, median_hourly_gap_pct,
            mean_bonus_gap_pct, median_bonus_gap_pct,
            pct_female_lower_quartile, pct_female_lower_mid_quartile,
            pct_female_upper_mid_quartile, pct_female_upper_quartile,
            pct_receiving_bonus_male, pct_receiving_bonus_female
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, tuple(row))

conn.commit()
cursor.close()
conn.close()

print("\nSuccessfully loaded into MySQL!")
print(f"Total rows inserted: {len(primark_clean)}")