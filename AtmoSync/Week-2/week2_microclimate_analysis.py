# AtmoSync: Micro-Climate Arbitrage Analytics - Week 2
# Compare micro-climate between 2 nearby locations and find arbitrage signal

import pandas as pd

data = {
    "location": ["Banjara Hills", "Banjara Hills", "Madhapur", "Madhapur",
                 "Kukatpally", "Kukatpally", "Gachibowli", "Gachibowli"],
    "date": ["2026-11-09"] * 8,
    "hour": [10, 15, 10, 15, 10, 15, 10, 15],
    "temp_c": [28.5, 33.2, 29.1, 34.8, 28.0, 32.5, 29.5, 35.4],
    "humidity_pct": [55, 42, 52, 38, 58, 45, 50, 36],
    "rain_mm": [0.0, 0.0, 0.0, 0.2, 0.0, 0.0, 0.0, 0.0]
}

df = pd.DataFrame(data)
print("Shape:", df.shape)
print(df.isnull().sum())

summary = df.groupby("location")[["temp_c", "humidity_pct"]].mean().round(2)
print("\nLocation Summary:\n", summary)

max_temp = df["temp_c"].max()
min_temp = df["temp_c"].min()
spread = max_temp - min_temp
print(f"\nMax Temp: {max_temp} C, Min Temp: {min_temp} C")
print(f"Micro-climate Spread: {spread:.1f} C")

if spread > 2.0:
    hottest = df.loc[df["temp_c"].idxmax(), "location"]
    coolest = df.loc[df["temp_c"].idxmin(), "location"]
    print(f"ARBITRAGE SIGNAL: {hottest} is {spread:.1f}C hotter than {coolest}")
    print("Action: Shift cold inventory / dynamic pricing to hotter zone")
else:
    print("No strong arbitrage signal today")
