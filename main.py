# install using pip
import requests
import json
import win32com.client as wincom

city = input('Enter the name of city: ')
# add your own api key
url = f'http://api.weatherapi.com/v1/current.json?key=e86675a0af9e404685d160825232108&q={city}'
r = requests.get(url)
weather_dic = json.loads(r.text)
print(f'The current temperature in {city} is', weather_dic['current']['temp_c'])
w = weather_dic['current']['temp_c']
s = wincom.Dispatch('SAPI.SpVoice')
s.Speak(f'The current temperature in {city} is {w}')



