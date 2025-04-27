import requests
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Configuration
api_key = "4eae97037b9bd531fb6608dc80fed456"  # Your API Key
city = "Mumbai"  # City for weather data

# API Request
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

# Error Handling
if response.status_code != 200:
    print("Failed to fetch data:", data.get("message", "Unknown error"))
    exit()

# Extract Weather Data
temperature = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']
weather_desc = data['weather'][0]['description']

# Display Weather Info
print(f"Weather in {city}:")
print(f"Temperature: {temperature}°C")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")
print(f"Condition: {weather_desc}")

# Simulated data for a week's temperature (for demonstration)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperature_week = [temperature + np.random.randint(-2, 3) for _ in days]  # Simulated variation

# Data Visualization
sns.set(style="whitegrid")
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Bar plot for current weather data
labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
values = [temperature, humidity, pressure]
sns.barplot(x=labels, y=values, palette="coolwarm", ax=ax[0])
ax[0].set_title(f"Current Weather Data in {city}")

# Line plot for weekly temperature
sns.lineplot(x=days, y=temperature_week, marker='o', ax=ax[1], color='blue')
ax[1].set_title("Temperature Variation Over the Week")
ax[1].set_ylabel("Temperature (°C)")

# Save the graph as an image
plt.savefig(f"{city}_weather.png")

# Show the graph
plt.show()
