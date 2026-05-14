import pandas as pd
import os

data = [
    {
        "year": 2019,
        "revenue_gbp_m": 7792,
        "operating_profit_gbp_m": 913,
        "operating_margin_pct": 11.7,
        "store_count": 373,
        "employee_count": 68000,
        "like_for_like_growth_pct": 4.0,
        "selling_space_sqft_m": 15.6
    },
    {
        "year": 2020,
        "revenue_gbp_m": 5765,
        "operating_profit_gbp_m": 362,
        "operating_margin_pct": 6.3,
        "store_count": 384,
        "employee_count": 70000,
        "like_for_like_growth_pct": -24.0,
        "selling_space_sqft_m": 16.1
    },
    {
        "year": 2021,
        "revenue_gbp_m": 5765,
        "operating_profit_gbp_m": 136,
        "operating_margin_pct": 2.4,
        "store_count": 398,
        "employee_count": 71000,
        "like_for_like_growth_pct": -12.0,
        "selling_space_sqft_m": 16.8
    },
    {
        "year": 2022,
        "revenue_gbp_m": 7723,
        "operating_profit_gbp_m": 756,
        "operating_margin_pct": 9.8,
        "store_count": 408,
        "employee_count": 73000,
        "like_for_like_growth_pct": 12.9,
        "selling_space_sqft_m": 17.3
    },
    {
        "year": 2023,
        "revenue_gbp_m": 9008,
        "operating_profit_gbp_m": 1072,
        "operating_margin_pct": 11.9,
        "store_count": 432,
        "employee_count": 78000,
        "like_for_like_growth_pct": 8.5,
        "selling_space_sqft_m": 17.9
    },
    {
        "year": 2024,
        "revenue_gbp_m": 9448,
        "operating_profit_gbp_m": 1108,
        "operating_margin_pct": 11.7,
        "store_count": 451,
        "employee_count": 82000,
        "like_for_like_growth_pct": 4.0,
        "selling_space_sqft_m": 18.8
    },
]

df = pd.DataFrame(data)

print("--- Primark Financials Dataset ---")
print(df.to_string(index=False))

os.makedirs("/Users/rohantanwar/Downloads/Primark/Cleaned_Data", exist_ok=True)
df.to_csv("/Users/rohantanwar/Downloads/Primark/Cleaned_Data/primark_financials.csv", index=False)
print("\nSaved to Cleaned_Data/primark_financials.csv")