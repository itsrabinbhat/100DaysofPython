# with open('weather_data.csv') as file:
#     data = file.readlines()
#
# print(data)

# import csv
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     temperatures = []
#
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['temp'].to_list())

# Get data from row

# print(data[data.temp == data.temp.max()])


# def f(x):
#     x = x * 1.8 + 32
#     return float(x)
#
#
# monday = data[data.day == 'Monday']
# print(monday.temp.apply(f))

# Creating csv file from dict
data_dict = {
    'students': ["Hary", "Amy", "John"],
    'scores': [45, 68, 89]
}

data = pandas.DataFrame(data_dict)
data.to_csv('new_data.csv')
