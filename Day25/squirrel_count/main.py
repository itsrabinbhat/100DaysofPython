import pandas

data = pandas.read_csv('./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrel = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrel = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel = len(data[data['Primary Fur Color'] == 'Black'])

fur_color_dict = {
    'Fur color': ['gray', 'cinnamon', 'black'],
    'Count': [gray_squirrel, cinnamon_squirrel, black_squirrel]
}

# for color in fur_color_list:
#     if color == 'Gray':
#         fur_color_dict['Count'][0] += 1
#     elif color == 'Cinnamon':
#         fur_color_dict['Count'][1] += 1
#     elif color == 'Black':
#         fur_color_dict['Count'][2] += 1

fur_color_data = pandas.DataFrame(fur_color_dict)
fur_color_data.to_csv('squirrel_count.csv')
