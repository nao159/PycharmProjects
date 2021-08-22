import requests

response = requests.get("https://valorant-api.com/v1/agents")
data = response.json()

values = 0
for value in data["data"]:
    values += 1

for value in range(0, values - 1):
    print(f"Character '{data['data'][value]['displayName']} is {data['data'][value]['isPlayableCharacter']}")