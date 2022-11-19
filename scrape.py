import requests
from bs4 import BeautifulSoup
import json


def get_names():

    
    response = requests.get(f"https://time.com/collection/100-most-influential-people-2021/")

    soup = BeautifulSoup(response.text, "html.parser")

    names = soup.select(".section-list__item-headline")

    others = soup.select(".section-list__item-byline")
    # print(names)

    data = []
    collection = [item.getText().strip() for item in names]

    for item in collection:
        if len(item) > 30:
            data.append(item)

    more = [item.getText()[3:] for item in others]

    # print(collection)
    # print (more)
    # print(data)
    # print(len(collection[20]))

    collection = set(collection)
    more = set(more)

    final = collection | more

    final2 = get_2022()

    result = final | final2

    result = list(result)
    result = sorted(result)


    data = dict()
    row = dict()
    n = 1
    for item in result:

        # if len(item) > 30: 
        #     continue
        row['name'] = item
        data[n] = row["name"]
        n += 1

    with open ("final_list.json",'w', encoding='utf-8') as file:
        file.write(json.dumps(data, indent=4))

def get_2022():
    response = requests.get(f"https://time.com/collection/100-most-influential-people-2022/")

    soup = BeautifulSoup(response.text, "html.parser")

    names = soup.select(".section-list__item-headline")

    others = soup.select(".section-list__item-byline")
    # print(names)

    data = []
    collection = [item.getText().strip() for item in names]

    for item in collection:
        if len(item) > 30:
            data.append(item)

    more = [item.getText()[3:] for item in others]

    collection = set(collection)
    more = set(more)

    final = collection | more

    return final

get_names()


