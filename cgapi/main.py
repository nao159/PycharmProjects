import requests

response = requests.get("https://valorant-api.com/v1/weapons/skins")
data = response.json()

values = 0
for _ in data["data"]:
    values += 1

print(values)
for value in range(0, values - 1):
    converted_data = data["data"][value]["displayName"]
    if "Vandal" in converted_data:
        print(converted_data)