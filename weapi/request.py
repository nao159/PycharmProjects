import requests
from tkinter import *
import os


city_name = "Saint Petersburg"
params = {
    "lon": 30.2642,
    "lat": 59.8944,
    "appid": "460461fd14f0ca1f5810ae55dbd49e8d",
    "lang": "ru"
}
lon = 30.2642
lat = 59.8944
API_key = "460461fd14f0ca1f5810ae55dbd49e8d"
#response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}")
response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=params)
print(response.status_code)
data = response.json()
print(data)
if data["current"]["weather"][0]["id"] < 700:
    print("bring umbrella")


window = Tk()
window.title("Weather")
window.minsize(width=500, height=500)

window.mainloop()