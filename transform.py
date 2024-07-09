import pandas as pd
import json

def load_data_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def transform_data(data):
    # Handle nested JSON structures flexibly
    if 'weather' in data and len(data['weather']) > 0:
        weather_description = data['weather'][0]['description']
    else:
        weather_description = 'Not available'
    
    # Extract relevant fields
    transformed_data = {
        'City': data.get('name', 'Unknown'),
        'Temperature': data['main']['temp'] - 273.15 if 'main' in data and 'temp' in data['main'] else None,
        'Pressure': data['main']['pressure'] if 'main' in data and 'pressure' in data['main'] else None,
        'Humidity': data['main']['humidity'] if 'main' in data and 'humidity' in data['main'] else None,
        'Weather_Description': weather_description,
        'Wind_Speed': data['wind']['speed'] if 'wind' in data and 'speed' in data['wind'] else None,
        'DateTime': pd.to_datetime(data['dt'], unit='s') if 'dt' in data else None
    }
    
    # Convert to DataFrame
    df = pd.DataFrame([transformed_data])
    
    return df

def save_data_to_csv(df, filename):
    if not df.empty:
        df.to_csv(filename, index=False)
        print("Data transformation and saving to CSV file successful.")
    else:
        print("No data to save.")

# Load extracted data
weather_data = load_data_from_file('weather_data.json')

# Transform data
transformed_data = transform_data(weather_data)

# Save transformed data to a CSV file
save_data_to_csv(transformed_data, 'transformed_weather_data.csv')
