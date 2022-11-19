"""Sourcing from a Celebrity API
API Ninjas - https://api.api-ninjas.com/v1/celebrity
"""

import requests
from occupation_json import occupation_categories


class CelebrityApi:
    """ Sourcing Class
    This is the main class and it handle the searching and the VIP score calculation.
    """

    def __init__(self):
        self.api_key = 'bBsLtDyj8uxzThYiw1HndQ==RWFIxB620FL6jRbC'

    def process(self, name, gender=None, age=None, occupation=None):
        """ Main function
        It searches the celebrity api and r
        
        Args:
            name (str): VIP (celebrity) name to lookup.
            gender (str | None): Gender of celebrity.
            age (int | None): Age of celebrity.
            occupation (str | None): Occupation of celebrity
        
        Return:
            List of Dictionaries in the below format:
            {
                'name': str,
                'age': int,
                'gender': str,
                'occupation': str,
                'vip_score': int
            }
            or [] is no result was found
        
        """
        if age is not None:
            age = int(age)
        else:
            age = age
        api_url = 'https://api.api-ninjas.com/v1/celebrity?name={}'.format(name['name'])
        """This is the search endpoint of the celebrity api"""

        response = requests.get(api_url, headers={'X-Api-Key': '{}'.format(self.api_key)})
        filtered = []
        return_params = {'name', 'age', 'gender', 'occupation'}

        if response.status_code == requests.codes.ok:
            data = response.json()
            # print(data)
            for celeb in data:
                try:
                    if all(param is None for param in [gender, age, occupation]):
                        # No parameter provided (except for name).
                        filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                        continue
                    elif all(param is not None for param in [gender, age, occupation]):
                        # All parameters (Gender, Occupation and Age) provided.
                        if celeb['gender'] == gender.lower() and celeb['age'] == age and occupation in celeb['occupation']:
                            filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                            continue
                    elif all(param is not None for param in [gender, age]):
                        # Only Gender and Age provided.
                        if celeb['gender'] == gender.lower() and celeb['age'] == age:
                            filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                            continue
                    elif all(param is not None for param in [gender, occupation]):
                        # Only occupation and Gender provided
                        if celeb['gender'] == gender.lower() and occupation in celeb['occupation']:
                            filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                            continue
                    elif all(param is not None for param in [occupation, age]):
                        if occupation in celeb['occupation'] and celeb['age'] == age:
                            filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                            continue
                        # else:
                        #     print('Occupation and Age provided, user Not found!!!')
                    elif occupation is not None:
                        if occupation in celeb['occupation']:
                            filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                            continue
                        # else:
                        #     print('Only Occupation provided, user Not found!!!')
                    elif gender is not None:
                        if celeb['gender'] == gender:
                            filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                            continue
                        # else:
                        #     print('Only Gender provided, user Not found!!!')
                    elif age is not None:
                        if celeb['age'] == age:
                            filtered.append({key: celeb[key] for key in celeb.keys() & return_params})
                            continue
                        # else:
                        #     print('Only Age provided, user Not found!!!')
                except KeyError:
                    # This is because the returned data is unclean.
                    # The response parameters are not the same for all items.
                    continue
            
            print('{} user(s) found'.format(len(filtered)))
            return self.vip_score(filtered)

        else:
            # api call unsuccessful
            return []
    
    def vip_score(self, filtered_list):
        """Calculates the VIP score
        It using the occupation of the celebrity to calculate the vip score

        Args:
            filtered_list (List): the list of filtered result
        
        Return:
            List of VIPs with their VIP scores.

        """

        for celeb in filtered_list:
            try:
                celeb_occ_scores = []
                for occupation in celeb['occupation']:
                    for category in occupation_categories:
                        if occupation in occupation_categories[category]['occupations']:
                            celeb_occ_scores.append(occupation_categories[category]['popularity_score'])
                celeb['vip_score'] = max(celeb_occ_scores)

                # pick the first occupation
                celeb['occupation'] = celeb['occupation'][0]

            except KeyError:
                # celeb net_worth not included in the response
                celeb['vip_score'] = 0
                continue
        
        return filtered_list
