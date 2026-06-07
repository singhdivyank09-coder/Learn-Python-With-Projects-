import requests #this module helps to access urls

def get_weather(city): #creating function to access weather information using wttr.in API
    # format=j1 specifies that we want the response in JSON format
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    
    # Check if the HTTP request was successful
    if response.status_code != 200:
        print(f"Error: Could not retrieve weather data (status code {response.status_code})")
        return False
        
    try:
        data = response.json()
    except Exception:
        print("Error: Could not parse response as JSON.")
        return False
        
    # Extracting current conditions
    current = data.get("current_condition", [{}])[0]
    temp = current.get("temp_C", "N/A")
    feels_like = current.get("FeelsLikeC", "N/A")
    humidity = current.get("humidity", "N/A")
    wind_speed = current.get("windspeedKmph", "N/A")
    
    # Extracting weather description
    descriptions = current.get("weatherDesc", [])
    description = descriptions[0].get("value", "N/A") if descriptions else "N/A"
    
    # Extracting location details
    area_info = data.get("nearest_area", [{}])[0]
    area_name = area_info.get("areaName", [{}])[0].get("value", "N/A") if area_info.get("areaName") else "N/A"
    region = area_info.get("region", [{}])[0].get("value", "N/A") if area_info.get("region") else "N/A"
    country = area_info.get("country", [{}])[0].get("value", "N/A") if area_info.get("country") else "N/A"
    
    # Displaying weather report
    print("\n" + "=" * 40)
    print(f" WEATHER FOR: {area_name.upper()}, {region.upper()}, {country.upper()}")
    print("=" * 40)
    print(f"Temperature   : {temp}°C")
    print(f"Feels Like    : {feels_like}°C")
    print(f"Condition     : {description.strip()}")
    print(f"Humidity      : {humidity}%")
    print(f"Wind Speed    : {wind_speed} km/h")
    print("=" * 40)
    return True

def main():
    city = input("enter city name : ").strip()
    if not city:
        print("City name cannot be empty.")
        return
        
    get_weather(city)

if __name__ == "__main__":
    main()
