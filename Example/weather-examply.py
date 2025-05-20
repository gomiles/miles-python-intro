import requests
import matplotlib.pyplot as plt
import numpy as np

# Coordinates for Dubai
latitude = 25.276987
longitude = 55.296249

# Open-Meteo API endpoint for 7-day forecast
url = (
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}"
    "&daily=temperature_2m_min,temperature_2m_max&timezone=auto"
)

response = requests.get(url)
data = response.json()

# Extract the relevant data
dates = data['daily']['time']
temps_min = data['daily']['temperature_2m_min']
temps_max = data['daily']['temperature_2m_max']

print("7-Day Weather Forecast for Dubai:")
for date, tmin, tmax in zip(dates, temps_min, temps_max):
    print(f"{date}: Min {tmin}°C / Max {tmax}°C")

# Visualization using matplotlib
x = np.arange(len(dates))  # the label locations

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, temps_min, marker='o', label='Min Temp (°C)', color='skyblue')
ax.plot(x, temps_max, marker='o', label='Max Temp (°C)', color='orange')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Temperature (°C)')
ax.set_title('7-Day Weather Forecast for Dubai')
ax.set_xticks(x)
ax.set_xticklabels(dates, rotation=45)
ax.legend()

fig.tight_layout()
plt.show()
