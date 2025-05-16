import requests

#====================================

# You should enter your API key here
# Sign up to get a free key:
#https://weatherstack.com/

try : 
	API_KEY = "Enter_Your_API_Here"
# Example: "abc123xyz"
except Exception as e:
    print("Erroe: ", e)

#====================================
#====================================

# You should enter your city name here
# Example: "Nablus", "London", etc.
city = input("Enter your city name: ")
#====================================

# Optional: If you want to use coordinates instead of city name
try:
    lat = float(input("Enter latitude :  "))
    lon = float(input("Enter longitude : "))
except ValueError:
    print("")
    exit()

# === Choose one of the URLs below === #

# Use coordinates (latitude, longitude)
url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={lat},{lon}&units=m"

# Or use city name only (uncomment to use this instead)
# url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}&units=m"
#====================================

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

# Check if data contains 'current' weather info

        if "current" in data:
            temp = data['current']['temperature']
            desc = data['current']['weather_descriptions'][0] if data['current']['weather_descriptions'] else "No description"
            name = data['location']['name']
            wind = data['current']['wind_speed']
            hum = data['current']['humidity']

            print(f"Weather in {name}:\n- {desc}\n- Temp: {temp}°C\n- Wind: {wind} km/h\n- Humidity: {hum}%")
        
# If there's an API error (e.g. invalid API key, limit reached)

        elif "error" in data:
            print("API error:", data["error"]["info"])
        
        else:
            print("Unexpected API response format.")
    else:
        print("Failed to connect to the API. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)