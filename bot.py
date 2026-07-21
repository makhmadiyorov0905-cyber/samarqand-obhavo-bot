import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

url = (
    f"https://api.openweathermap.org/data/2.5/weather"
    f"?q=Samarkand&appid={WEATHER_API_KEY}&units=metric&lang=uz"
)

response = requests.get(url)
data = response.json()

if data.get("cod") != 200:
    raise Exception(f"API xatosi: {data}")

temp = data["main"]["temp"]
feels = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["description"]

text = f"""🌤 Samarqand bugungi ob-havosi

🌡 Harorat: {temp}°C
🤗 His qilinishi: {feels}°C
💧 Namlik: {humidity}%
☁️ Holat: {weather}
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": text
    }
)

print("Ob-havo muvaffaqiyatli yuborildi.")
