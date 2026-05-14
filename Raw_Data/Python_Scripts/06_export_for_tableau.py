import mysql.connector
import pandas as pd
import os

output_folder = "/Users/rohantanwar/Downloads/Primark/Cleaned_Data/Tableau_Exports"
os.makedirs(output_folder, exist_ok=True)

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rohan_123!!!",
    database="primark_project"
)

queries = {
    "01_revenue_growth": """
        SELECT 
            year,
            revenue_gbp_m,
            operating_profit_gbp_m,
            operating_margin_pct,
            store_count,
            employee_count,
            like_for_like_growth_pct,
            selling_space_sqft_m,
            ROUND((revenue_gbp_m - LAG(revenue_gbp_m) OVER (ORDER BY year)) 
                / LAG(revenue_gbp_m) OVER (ORDER BY year) * 100, 1) AS yoy_revenue_growth_pct
        FROM primark_financials
        ORDER BY year
    """,
    "02_gender_pay_trend": """
        SELECT
            reporting_year,
            mean_hourly_gap_pct,
            median_hourly_gap_pct,
            mean_bonus_gap_pct,
            median_bonus_gap_pct,
            pct_female_lower_quartile,
            pct_female_lower_mid_quartile,
            pct_female_upper_mid_quartile,
            pct_female_upper_quartile,
            pct_receiving_bonus_male,
            pct_receiving_bonus_female,
            ROUND(pct_female_upper_quartile - LAG(pct_female_upper_quartile) 
                OVER (ORDER BY reporting_year), 1) AS upper_quartile_change
        FROM primark_gender_pay
        ORDER BY reporting_year
    """,
    "03_store_expansion_by_country": """
        SELECT
            country,
            region,
            SUM(stores_opened) AS total_stores_opened,
            MAX(total_stores) AS stores_in_2024,
            MIN(total_stores) AS stores_in_2019,
            MAX(total_stores) - MIN(total_stores) AS net_growth,
            MAX(selling_space_sqft_m) AS current_selling_space
        FROM primark_store_expansion
        GROUP BY country, region
        ORDER BY net_growth DESC
    """,
    "04_store_expansion_by_year": """
        SELECT
            year,
            country,
            region,
            total_stores,
            stores_opened,
            selling_space_sqft_m
        FROM primark_store_expansion
        ORDER BY year, country
    """,
    "05_sustainability_progress": """
        SELECT
            reporting_year,
            sustainable_materials_pct,
            recycled_fibres_pct,
            ghg_reduction_vs_2019_pct,
            scope1_2_reduction_pct,
            supplier_audits_total,
            workers_reached_programmes,
            cotton_project_farmers,
            ROUND(sustainable_materials_pct - LAG(sustainable_materials_pct) 
                OVER (ORDER BY reporting_year), 1) AS materials_improvement
        FROM primark_sustainability
        ORDER BY reporting_year
    """,
    "06_combined_overview": """
        SELECT
            f.year,
            f.revenue_gbp_m,
            f.operating_profit_gbp_m,
            f.operating_margin_pct,
            f.store_count,
            f.employee_count,
            f.like_for_like_growth_pct,
            g.mean_hourly_gap_pct,
            g.median_hourly_gap_pct,
            g.pct_female_upper_quartile
        FROM primark_financials f
        LEFT JOIN primark_gender_pay g ON f.year = g.reporting_year
        ORDER BY f.year
    """
}

for filename, query in queries.items():
    df = pd.read_sql(query, conn)
    filepath = os.path.join(output_folder, f"{filename}.csv")
    df.to_csv(filepath, index=False)
    print(f"Exported {filename}.csv — {len(df)} rows")

conn.close()
print(f"\nAll files saved to: {output_folder}")
print("Ready to import into Tableau!")