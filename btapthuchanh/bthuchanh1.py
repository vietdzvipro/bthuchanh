import requests
import pandas as pd

# --- Lấy dữ liệu từ API ---
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "past_days": 10,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

response = requests.get(url, params=params)
data = response.json()

# --- Xử lý và lưu dữ liệu ---
latitude = data["latitude"]
longitude = data["longitude"]
hourly = data["hourly"]

df = pd.DataFrame({
    "time": hourly["time"],
    "temperature_2m": hourly["temperature_2m"],
    "relative_humidity_2m": hourly["relative_humidity_2m"],
    "wind_speed_10m": hourly["wind_speed_10m"]
})

df["latitude"] = latitude
df["longitude"] = longitude

# Lưu vào file CSV
df.to_csv("weather_data.csv", index=False)
print("Đã lưu dữ liệu vào weather_data.csv")

# --- Tính tổng đến ngày 29-04-2025 ---
df["time"] = pd.to_datetime(df["time"])
filtered_df = df[df["time"] <= "2025-04-29 23:59:59"]

total_temp = filtered_df["temperature_2m"].sum()
total_humidity = filtered_df["relative_humidity_2m"].sum()
total_wind = filtered_df["wind_speed_10m"].sum()

print("\nTổng các giá trị đến ngày 29-04-2025:")
print(f"- Tổng temperature_2m: {total_temp}")
print(f"- Tổng relative_humidity_2m: {total_humidity}")
print(f"- Tổng wind_speed_10m: {total_wind}")
