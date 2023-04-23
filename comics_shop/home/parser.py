from bs4 import BeautifulSoup
import requests, json, csv

all_comics = []
number = 1
num = 1
for i in range(1, 2):
    url = f'https://www.chookandgeek.ru/collection/dc_rus?page={i}'
    req = requests.get(url)

    # with open(f'dc/{i}.html', 'w', encoding='utf-8') as file:
    #     file.write(req.text)

    with open(f'other/dc/{i}.html', encoding='utf-8') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    small_comics = soup.find_all(class_='product_preview product_preview--collection')
    for product in small_comics:
        # print(product)
        comics = product.find('a').get('href')
        full_link = 'https://www.chookandgeek.ru' + comics
        comics_request = requests.get(full_link).text
        page = BeautifulSoup(comics_request, 'lxml')

        title = page.find('h1').text.strip().replace('\n', '')
        try:
            cover = page.find('img', class_='js-product_gallery-preview_image lg-hidden md-hidden').get('src')
        except:
            cover = None

        try:
            description = page.find(class_='product-description editor').text.replace('\n', '')
        except:
            description = None

        try:
            price = page.find(class_='prices-current js-prices-current').text.strip().replace('\n', '')
        except:
            price = None

        parametr_name = page.find(class_='product-properties lg-grid-12').find_all('td',
                                                                                   class_='property-title lg-grid-3 xs-grid-4 mc-grid-12 padded-right padded-bottom mc-padded-zero-right mc-padded-top')
        parametr_name = [i.text.replace('\n', '').strip()[:-1] for i in parametr_name]
        # print(parametr_name)
        parametr_value = page.find(class_='product-properties lg-grid-12').find_all('td',
                                                                                    class_='property-values lg-grid-9 xs-grid-8 mc-grid-12 padded-left padded-bottom mc-padded-zero-left')
        parametr_value = [' '.join(i.text.replace('\n', '').strip().split()) for i in parametr_value]
        # print(parametr_value)
        # print(f)
        parametr_list = list(zip(parametr_name, parametr_value))
        # parametr_list = ['Издательство', 'Эксмо', 'Художник', ]
        dict_param = {}
        for name, value in parametr_list:
            dict_param[name] = value
        # print(dict_param)

        # print(description)
        # print(cover)
        # print(comics_request.text)
        # print(comics)
        # title = product.find('a', class_='product_preview-link').get('title')
        # print(title)
        # cover = product.find('img').get('src')
        # print(cover)
        # with open(f'dc/covers/{number}.jpg', 'wb') as file:
        # file.write(requests.get(cover).content)
        # number += 1
        # price = product.find(class_="prices-current").text.strip()
        # print(price)
        main_dict = {'id': num,
                     'title': title,
                     'cover': cover,
                     'price': price,
                     'description': description,
                     }
        for name in dict_param:
            name1 = name
            if name == 'Автор/Сценарист':
                name1 = 'Автор'
            main_dict[name1] = dict_param[name]
        main_dict['buy_status'] = 0
        all_comics.append(main_dict)
        print(num)
        num += 1

    # print(small_comics[0])
    # all_comics += small_comics

with open('other/comics.json', 'w', encoding='utf-8') as file:
    json.dump(all_comics, file, ensure_ascii=False)
# with open('comics.csv', 'w', encoding='utf-8') as file:
#     fieldnames = all_comics[0].keys()
#     # writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer = csv.writer(file)
#     for dict_comics in all_comics:
#         writer.writerow(dict_comics.values())
# print(all_comics[0])

# print(comics[0])
# for product in comics:
#     print(product)
# print(comics)
