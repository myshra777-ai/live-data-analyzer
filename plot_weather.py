import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
df = pd.read_csv("weather_data.csv")

# Plot temperature trend
plt.plot(df["timestamp"], df["temperature"], marker='o', linestyle='-', color='blue')
plt.xticks(rotation=45)
plt.title("Temperature Trend in Indore")
plt.xlabel("Timestamp")
plt.ylabel("Temperature (°C)")
plt.tight_layout()
plt.grid(True)
plt.show()