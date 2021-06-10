txt = "Hello" [::-1]
print(txt)

txt = "Hello" [2:4:]
print(txt)

txt = "Hello" [2::-1]
print(txt)


#https://www.domaonline.com/data-integration/
#https://openweathermap.org/current
#https://cojeapi.cz/03-zakladni-pojmy.html


import requests

endpoint = "https://api.openweathermap.org/data/2.5/weather"
API_key = "340b0d536435130e8aa8a75d2cba38bd"

params = {
    "lat": 35,
    "lon": 139,
    "appid": API_key,
}

response = requests.get(endpoint, params=params)
print(response.json())

#https://blockchain.info/ticker
#free API example