import pandas as pd
import os

df=pd.read_csv("raw_data/covid_data_samples.csv")
df_cleaned=df.dropna()

df_cleaned.to_csv("output_data/cleaned_covid_data.csv",index=False)

os.makedirs("demo folder", exist_ok=True)

# Total Confirmed, Deaths, Recovered by Country
df_by_country=df_cleaned.groupby("Country")[["Confirmed", "Deaths", "Recovered"]].sum()
df_by_country.to_csv("output_data/cleaned_order_by_country.csv")

# daily trends of cases
df_order_by_daily_trend=df_cleaned.groupby("Date")[["Confirmed", "Deaths"]].sum()
df_order_by_daily_trend.to_csv("output_data/order_by_daily_trend.csv")

print("Cleaned data saved successfully!")