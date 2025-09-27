import pandas as pd

df = pd.read_csv("weather_data.csv")
print("Columns:", df.columns.tolist())
print("\nFirst few rows:")
print(df.head())