import requests
from decouple import config

headers = {"X-Api-Key": config("NINJA_API")}
base_url = "https://api.api-ninjas.com/v1/celebrity?name="


def celebrity_api2(name, *args, **kwargs):

    response = requests.get(url=base_url+name, headers=headers)

    result = response.json()

    new_dict = dict() 
    
    new_list = list()

    for item in result:

        new_dict['name'] = item['name']
        new_dict['age'] = item.get('age', None)
        new_dict['gender'] = item.get('gender', None)
        new_dict['occupation'] = item.get('occupation', [])
        new_dict['vip_score'] = determine_vip_score(item.get('net_worth', 1))
        
        new_list.append(new_dict.copy())
        
    return new_list


def determine_vip_score(value):
    if value >= 70000000:
        return 3
    elif value <=1000000:
        return 1
    else:
        return 2  