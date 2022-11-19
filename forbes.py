import json
import re

from pyforbes import ForbesList


class ForbesVip():

    def make_result(self, data: str) -> dict:
        local_dict = {}
        data_con = data.split(";")
        for i in data_con:
            j = i.split(":")
            local_dict[j[0]] = j[1]
        return self.dict_to_json(local_dict)

    def dict_to_json(self, data: dict):
        json_data = json.dumps(data)
        # return dict(json.loads(json_data))
        return data

        pass

    def process(self, pname):
        frb_list = ForbesList()
        result_list = []

        df = frb_list.get_df('billionaires')
        # js = frb_list.get_df('thailand-billionaires',year=2020)

        # with open("frb400.csv", "w") as ll:
        # js.to_csv('frb400.csv')

        len = df.firstName.size
        scorer = ['Automotive', 'Technology', 'Fashion & Retail', 'Finance & Investments',
                  'Diversified', 'Media & Entertainment', 'Telecom', 'Food & Beverage',
                  'Logistics', 'Real Estate', 'Metals & Mining', 'Manufacturing',
                  'Gambling & Casinos', 'Healthcare', 'Service', 'Energy',
                  'Construction & Engineering', 'Sports', ]
        score = {
            'Automotive': 6, 'Technology': 7, 'Fashion & Retail': 2, 'Finance & Investments': 4,
            'Diversified': 8, 'Media & Entertainment': 2, 'Telecom': 6, 'Food & Beverage': 9,
            'Logistics': 3, 'Real Estate': 3, 'Metals & Mining': 7, 'Manufacturing': 9,
            'Gambling & Casinos': 5, 'Healthcare': 8, 'Service': 4, 'Energy': 9,
            'Construction & Engineering': 7, 'Sports': 4,
        }

        for i in range(len):
            name = str(df.firstName[i]) + " " + str(df.lastName[i])
            industry = str(df.category[i])
            country = str(df.country[i])
            age = int(df.age[i]) if df.age[i] >= 0 else 0
            gender = "Male" if df.gender[i] == "M" else "Female"
            vip_score = 1

            for indus in scorer:
                if indus == industry:
                    vip_score += score[indus]

            # data = f"name:{name};occupation:[{industry}];country:{country};age:{age};gender:{gender};vip_score:{vip_score}"
            diction = {
                "name": name,
                "occupation": [industry],
                "country": country,
                "age": age,
                "gender": gender,
                "vip_score": vip_score,
            }
            # compile name passed to regex pattern
            namep = re.compile(pname['name'].lower())

            # search if name pattern is in the name variable
            if namep.search(name.lower()):
                result_list.append(diction)
                # result_list.append(self.make_result(data))
        return result_list


vip = ForbesVip()