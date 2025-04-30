import requests
from utils.convert_temp import convert_temp
from utils.convert_wind_speed import convert_wind_speed
from services.print_log import save_log

def fetch_weather(token: str, city: str):
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}"
    
    try: 
        #print(url)
        response = requests.get(url)
        #print(response)
        data = response.json()
        #print(data)
        
        save_log(response.status_code)
        
        weather = {
            "name": data["name"],
            "temp": convert_temp(data["main"]["temp"]),
            "feels_like": convert_temp(data["main"]["feels_like"]),
            "humidity": data["main"]["humidity"],
            "wind_speed": convert_wind_speed(data["wind"]["speed"])
        }
        
        return weather
        
    except Exception as e:
        print(token, city)