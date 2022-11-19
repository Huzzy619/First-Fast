# from interview import twitter_api, facebook_api, celebrity_api


def vip_calc(results:list, **kwargs):
    # making sure the argument passed is a list
    if not isinstance(results, list):
        return "result data must be a list type"
    # check if the results is an empty list
    if not results or results==[]:
        return []
    result_list_count = []
    for item in results:
        result_list_count.extend(item)
    # check the list count, if it's just one, it means the user are unique 
    # as it's not expected for a user to have multiple account accross a platform, 
    # hence it returns the single list
    if results.count(result_list_count) == 1:
        return result_list_count

    people = {}
    people_scores = {}
    # iterate over the lists of the dictionary list so we can have access
    #  to individual list in the results list
    for result in results:
        # create a site ID for each list of result passed
        site = f"site_{results.index(result)}"
        for person in result: 
            name = person.get('name', '')
            email = person.get('email', '')
            age = person.get('age', '')
            gender = person.get('age', '')
            occupation = person.get('age', '')
            # create a person ID for each dictionary in the iterated list
            person_id = f"{name}_{email}_{age}_{gender}_{occupation}"
            # add the person ID as a key to the people dictionary
            people.setdefault(person_id, {})
            people[person_id][site] = person
    for person, data in people.items():
        scores = [user['vip_score'] for user in data.values()]
        person_avg_vip_score = sum(scores) / len(scores)
        person_data = list(data.values())[0]
        person_data['vip_score'] = int(person_avg_vip_score)
        people_scores[person] = person_data
    # returns the user details as it were in the dictionaries 
    # but with a new vip_score(average_vip_score)
    return list(people_scores.values())



