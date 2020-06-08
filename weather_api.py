import requests
city = input('Enter your city : ')
base_url = 'https://api.openweathermap.org/data/2.5/weather'
api_id = '9e4fba99f8449c52ab2347e51827f4fa'
url = f'{base_url}?q={city}&APPID={api_id}'
if city != "":
    res = requests.get(url)
    json_data = res.json()
    try:
        print(f"City : {json_data['name']}")
        print(f"current weather : {json_data['weather'][0]['main']}")
        # print(json_data['weather'][0]['description'])
    except KeyError as e:
        print("Error : City not found")
print('press any key to exit...')
a = input()
