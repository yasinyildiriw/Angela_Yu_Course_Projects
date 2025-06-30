#import csv

# with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperatures = []
#   for row in data:
#       if row[1] != "temp":
#           temperatures.append(int(row[1]))
#print(temperatures)
##############################################################################################
#import pandas
#data = pandas.read_csv("weather_data.csv")
#print(data["temp"])
#PANDAS KULLANMAK İŞLERİ ÇOK KOLAYLAŞTIRIYOR
###############################################################################################
# import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# sum=0
# for item in temp_list:
#     sum += item
# temp_average = sum/len(temp_list)
# print(temp_average)
# max_temp = data["temp"].max()
# print(max_temp)
# con = data["condition"].to_dict()
# print(con)
# print(data[data.temp == max_temp])
# monday = data[data.day == "Monday"]
# print(monday.temp)
