import csv


class AnimeData():

    def __init__(self, name, startDate, endDate, description, episodeCount, ageRating):

        self.name = name
        self.ongoingDate = startDate
        self.releaseDate = endDate
        self.description = description
        self.episodes = episodeCount
        self.ageRating = ageRating

    def write_anime_into_csv(file, data):
        """This function takes file name and data and makes a brand new csv file with given data"""
        with open(f"{file}.csv", "w") as file:
            keys = data[0].keys()
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
