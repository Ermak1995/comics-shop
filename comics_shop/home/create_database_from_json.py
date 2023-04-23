# import json
import pandas as pd

with open('other/comics.json', encoding='utf-8') as inputfile:
    df = pd.read_json(inputfile)

df.to_csv('other/comics.csv', encoding='utf-8', index=False)
# from models import Comics_from_json as Comics
# with open('home/other/comics.json', encoding='utf-8') as file:
#     data = json.load(file)
# # num = 1
# for dict_comics in data:
#     title = dict_comics['title']
#     cover = dict_comics['cover']
#     price = dict_comics['price']
#     description = dict_comics['description']
#     obj = Comics.objects.create(title=title, publisher = 1, cover=cover, price=price, description=description)
#     obj.save()
# print('OKAY')
