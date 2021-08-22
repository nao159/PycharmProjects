import csv
import pandas

#pandas_data = pandas.read_csv("weather_data.csv")
#print(pandas_data)
#print(pandas_data["temp"])

#print(pandas_data["temp"].mean())
#print(pandas_data["temp"].max())

#print(pandas_data[pandas_data["day"] == "Wednesday"])
# or pandas_data[pandas_data.day == "Wednesday"]
#print(pandas_data[pandas_data.temp == pandas_data.temp.max()])

#monday = pandas_data[pandas_data.day == "Monday"]
#monday_temp_F = monday.temp * 9 / 5 + 32
#print(monday_temp_F)

#new_dict = {
   # "students": ["maxim", "ilon", "mona"],
    #"score": [100, 75, 25]
#}

#new_data = pandas.DataFrame(new_dict)
#print(new_data)
#new_data.to_csv("new_data.csv")

#maxim = new_data[new_data.students == "maxim"]
#print(maxim.score)

squirrel_data = pandas.read_csv("Squirrel_Data.csv")
squirrel_colors = squirrel_data["Primary Fur Color"]
black_squirrel = len(squirrel_data[squirrel_colors == "Black"])
cinnamon_squirrel = len(squirrel_data[squirrel_colors == "Cinnamon"])
gray_squirrel = len(squirrel_data[squirrel_colors == "Gray"])
undefined_squirrel_color = len(squirrel_data) - black_squirrel - cinnamon_squirrel - gray_squirrel

squirrel_dict = {
    "Color": ["Black", "Cinnamon", "Gray"],
    "Count": [black_squirrel, cinnamon_squirrel, gray_squirrel]
}

squirrel_color_data = pandas.DataFrame(squirrel_dict)
print(squirrel_color_data)
