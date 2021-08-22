import requests
from datetime import *
import smtplib
from time import sleep


def is_night_and_close():
    my_location = {
        "lat": 59.928872,
        "lon": 30.348358,
        "formatted": 0
    }

    response = requests.get(f"https://api.sunrise-sunset.org/json", params=my_location)
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    time_now = datetime.now().hour

    sunrise_time = sunrise.split("T")[1].split(":")[0]
    sunset_time = sunset.split("T")[1].split(":")[0]

    iss = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data = iss.json()
    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lon = float(iss_data["iss_position"]["longitude"])

    lat_range = range(int(my_location["lat"]) - 5, int(my_location["lat"]) + 5)
    lon_range = range(int(my_location["lon"]) - 5, int(my_location["lon"]) + 5)

    if time_now > sunset_time or time_now < sunrise_time:
        if iss_lat in lat_range and iss_lon in lon_range:
            return True
    else:
        return False


while True:
    sleep(300)
    if is_night_and_close:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            MY_MAIL = "vainikkaxd@gmail.com"
            MY_PASS = "031099ma"
            connection.login(user=MY_MAIL, password=MY_PASS)
            connection.sendmail(from_addr=MY_MAIL, to_addrs=MY_MAIL, msg="Subject:Look up!\n\nHey, look at the sky!")
