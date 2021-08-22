import requests
import datetime as dt
pixela_endpoint = "https://pixe.la/v1/users"


params = {
    "token": "dolboeb_da_Da_DA_YA",
    "username": "arthas",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graphs = f"https://pixe.la/v1/users/{params['username']}/graphs"
graphs_params = {
    "id": "graph1",
    "name": "coding time",
    "unit": "hours",
    "color": "ajisai",
    "type": "float"
}

graphs_header = {
    "X-USER-TOKEN": "dolboeb_da_Da_DA_YA"
}
#response = requests.post(url=pixela_endpoint, json=params)
#print(response.text)
#response = requests.post(url=graphs, json=graphs_params, headers=graphs_header)
#print(response.text)

pixel_url = f"https://pixe.la/v1/users/arthas/graphs/graph1"
now = dt.datetime.now().date()
converted_now = str(now).replace("-", "")
pixel_url_updated = f"{pixel_url}/{converted_now}"
print(converted_now)
pixel_params = {
    "date": converted_now,
    "quantity": "15.0",

}

pixel_header = {
    "X-USER-TOKEN": "dolboeb_da_Da_DA_YA"
}
#response = requests.post(url=pixel_url, json=pixel_params, headers=graphs_header)
#print(response.text)

#response = requests.put(url=pixel_url_updated, json=pixel_params, headers=graphs_header)
#print(response.text)

response = requests.delete(url=pixel_url, json=pixel_params, headers=graphs_header)
print(response.text)