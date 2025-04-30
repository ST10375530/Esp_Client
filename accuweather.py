import requests

def get_weather(location_key):
    url = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}'
    params = {
        'apikey': 'fmwesWXlob2kVukt1FghBaalWlsZvc6k'
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    location_key = 'YOUR_LOCATION_KEY'  
    weather = get_weather(location_key)
    print(weather)
