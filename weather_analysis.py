import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("weather.csv")

# Display the first five rows
print("Weather Dataset:")
print(df.head())

# Display dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

# Calculate average temperature
avg_temp = np.mean(df["Temperature"])
print("\nAverage Temperature:", avg_temp)

# Find maximum and minimum temperatures
max_temp = np.max(df["Temperature"])
min_temp = np.min(df["Temperature"])

print("Maximum Temperature:", max_temp)
print("Minimum Temperature:", min_temp)

# Calculate average humidity
avg_humidity = np.mean(df["Humidity"])
print("Average Humidity:", avg_humidity)

# Calculate total rainfall
total_rainfall = np.sum(df["Rainfall"])
print("Total Rainfall:", total_rainfall)

# Find days with temperature above 28°C
hot_days = df[df["Temperature"] > 28]

print("\nDays with Temperature Above 28°C:")
print(hot_days)

# Find days with rainfall above 5 mm
rainy_days = df[df["Rainfall"] > 5]

print("\nDays with Rainfall Above 5 mm:")
print(rainy_days)

# Sort by temperature
sorted_weather = df.sort_values(
    by="Temperature",
    ascending=False
)

print("\nWeather Sorted by Temperature:")
print(sorted_weather)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate temperature standard deviation
std_temp = np.std(df["Temperature"])

print("\nTemperature Standard Deviation:", std_temp)

# Find hottest and coldest days
hottest_day = df.loc[df["Temperature"].idxmax()]
coldest_day = df.loc[df["Temperature"].idxmin()]

print("\nHottest Day:")
print(hottest_day)

print("\nColdest Day:")
print(coldest_day)
