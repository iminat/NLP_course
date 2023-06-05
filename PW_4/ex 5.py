import requests
import pandas as pd

# API endpoint and parameters
api_key = 'YOUR_API_KEY'
city = 'London'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

# Make API request
response = requests.get(url)
data = response.json()

# Print JSON data
print(data)

# Create DataFrame
df = pd.DataFrame(data)
print(df)