import pandas as pd

# data = pd.read_csv("Day - 25\weather_data.csv")
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(len(temp_list))

# #Calling the average 
# average = sum(temp_list) / len(temp_list)
# print(average)
# #Calling mean
# print(data["temp"].mean())

# #calling the max value
# print(data["temp"].max())

# #Get specific data in a row
# print(data[data.day=="Monday"])

# #Print the row of the data that has the maximum tempoerature of the week
# print(data[data.temp==data.temp.max()])

# #Get the temperature for monday in fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# #Create a dataframe from scratch
# data_dict = {
#    "students" : ["Stone", "Wisgens", "Angela", "Wikender"],
#    "scores": [76, 56, 65, 85]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("Day - 25\ new_datas.csv")

#Building dataframe for squirrel types
data = pd.read_csv("Day - 25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#fur_color = data[data.Color == "Primary Fur Color"]
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(black_squirrels_count)
print(grey_squirrels_count)
print(red_squirrels_count)

#Create a DataFrame
data_dict = {
   "Fur Color": ["Gray","Black", "Cinnamon"],
   "Count" : [grey_squirrels_count,black_squirrels_count, red_squirrels_count]
}

print(data_dict)
df = pd.DataFrame(data_dict)
df.to_csv("Day - 25\squirrel_count.csv")