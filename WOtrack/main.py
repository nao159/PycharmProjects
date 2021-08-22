import datetime as dt
import requests

API_ID = "2ede3f52"
API_KEY = "e94d8983f0c66319a27b6e2159c8ea7f"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
new_row_endpoint = "https://api.sheety.co/de32964600e1ab52d3838a34e73d0edd/myWorkouts/workouts"
sheety_endpoint = "https://api.sheety.co/de32964600e1ab52d3838a34e73d0edd/myWorkouts/workouts"
wo_headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
wo_params = {
    "query": "coding 2 hours",
    "gender": "Male",
    "weight_kg": 90,
    "height_cm": 170,
    "age": 21
}

response = requests.post(url=exercise_endpoint, json=wo_params, headers=wo_headers)
data = response.json()
print(data)

today_date = dt.datetime.now().strftime("%d%m/%Y")
now_time = dt.datetime.now().strftime("%X")


for activity in data['exercises']:
    activity = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": activity['name'].title(),
            "duration": activity['duration_min'],
            "calories": activity['nf_calories']
        }
    }

    activity_response = requests.post(url=sheety_endpoint, json=activity, auth=("Nao", "031099maW"))
    print(activity_response)