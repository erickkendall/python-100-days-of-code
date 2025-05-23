# Day 25 - Working with CSV Data and the Pandas Library
# 100 Days of Code - Python Pro Bootcamp

# Your code here
import csv
import pandas


# with open("./weather_data.csv", "r") as data_file:
#    data = data_file.readlines()

#with open("./weather_data.csv") as data_file:
#    data=csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        day, temp, condition = row
#        if temp != "temp":
#            temperatures.append(int(temp))
#
#    print(temperatures)
#
#data = pandas.read_csv("./weather_data.csv")
#print(data["temp"])
#
#data_dict = data.to_dict()
#print(data_dict)
#
#temp_list = data["temp"].to_list()
#print(temp_list)
#avg = data["temp"].mean()
#print(avg)
#average = sum(temp_list) / len(temp_list)
#print(average)
#
#maximum = data["temp"].max()
#print(f"maximum is {maximum}")
#
#print(data.condition)
#print(data[data.day == "Monday"])
#print(data[data.temp == data.temp.max()])
#
#celsius_series = data.temp.apply(lambda f:(f/32) * 5/9)
#print(celsius_series)
#
#data_dict = {
#    "students": ["Amy", "Ted", "Brian"],
#    "scores": [70,40,90]
#}
#
#data=pandas.DataFrame(data_dict)
#data.to_csv("new_data.csv")

df = pandas.read_csv("./Squirrel_Data_20250520.csv")
black_squirrel_count = len(df[df["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(df[df["Primary Fur Color"] == "Cinnamon"])
gray_squirrel_count = len(df[df["Primary Fur Color"] == "Gray"])

print(black_squirrel_count)
print(cinnamon_squirrel_count)
print(gray_squirrel_count)

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Count": [ black_squirrel_count, cinnamon_squirrel_count, gray_squirrel_count ]
}
df = pandas.DataFrame(data_dict)
df.to_csv("./squirrel_count.csv")

