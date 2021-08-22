import requests
from anime import AnimeData
from usefulTools import UsefulTools

API_PATH = "https://kitsu.io/api/edge/anime"

params_for_request = {
    "categories": "adventure",
    "page[limit]": 5
}

response = requests.get(url=API_PATH, params=params_for_request)
data = response.json()["data"]

anime_dict = []
for anime in data:
    name = anime['attributes']['canonicalTitle']
    startDate = anime['attributes']['startDate']
    endDate = anime['attributes']['endDate']
    description = anime["attributes"]["description"]
    episodeCount = anime["attributes"]["episodeCount"]
    ageRating = anime["attributes"]["ageRatingGuide"]
    new_item_dictionary = {
        "name": name,
        "ongoingDate": startDate,
        "releaseDate": endDate,
        "description": description,
        "episodes": episodeCount,
        "ageRating": ageRating
    }
    anime_dict.append(new_item_dictionary)


sorted_anime_dict = UsefulTools.sort_by(data_to_sort=anime_dict, sort_by="ongoingDate")
AnimeData.write_anime_into_csv(file="anime", data=sorted_anime_dict)