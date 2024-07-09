import requests
import json

# Replace with your actual API key
api_key = "6dc464a6c7f32aa049ffda37e05d4b02"
url = f"https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid={api_key}"

def extract_weather_data():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
        
# Extract data
weather_data = extract_weather_data()

# Save to a file
if weather_data:
    save_data_to_file(weather_data, "weather_data.json")
    print("Data extraction and saving to file successful.")
else:
    print("No data to save.")
