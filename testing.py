
from pprint import pprint
import json
import httpx
hey = {
    # "name": "barack obama",
    "age": 12,
    "gender": "male",
    "occupation": "politics",
    # "vip_score": 3,
},

hi = {
    # "name": "Bar Obama",
    "age": 12,
    "gender": "male",
    "occupation": "politics",
    # "vip_score": 8,
},


hey = json.dumps(hey)
hi = json.dumps(hi)

# print({hey} | {hi})


data = {
    "status": "success",
    "message": "new message sent",
    "data": {
        "sender_id": "619bab3b1a5f54782939d400",
        "emojis": [],
        "richUiData": {
            "blocks": [
                {
                    "key": "eljik",
                    "text": "Larry Gaaga",
                            "type": "unstyled",
                            "depth": 0,
                            "inlineStyleRanges": [],
                            "entityRanges": [],
                            "data": {}
                }
            ],
            "entityMap": {}
        },
        "files": [],
        "saved_by": [],
        "timestamp": 0,
        "created_at": "2022-02-01 19:20:55.891264",
        "room_id": "61e6855e65934b58b8e5d1df",
        "org_id": "619ba4671a5f54782939d384",
        "message_id": "61f98d0665934b58b8e5d286",
        "edited": False,
        "threads": []
    }
}


message = {
    "sender_id": "619baa7a1a5f54782939d395",
    "timestamp": 1669280975096,
    "emojis": [],
    "richUiData": {
        "blocks": [
            {
                "key": "melc",
                "text": "@dfelastevetest this a test on mentioning people",
                "type": "unstyled",
                "depth": 0,
                "inlineStyleRanges": [],
                "entityRanges":[
                    {
                        "offset": 0,
                        "length": 15,
                        "key": 0
                    }
                ],

                "data": {}
            }],
        "entityMap": {
            "0": {
                "type": "mention",
                "mutability": "SEGMENTED", "data":
                {"mention": {"name": "valenteeena",
                             "link": "valenteeena@gmail.com",
                             "avatar": "https://api.zuri.chat/files/profile_image/614679ee1a5607b13c00bcb7/614f06e6e35bb73a77bc2aa3/20211002190529_0.gif"
                             }
                 }
            },
            "1":
            {"type": "mention",
                "mutability": "SEGMENTED",
                "data": {
                    "mention": {
                        "name": "funkymikky4ril",
                        "link": "funkymikky4ril@yahoo.com",
                        "avatar": "https://api.zuri.chat/files/profile_image/614679ee1a5607b13c00bcb7/6146fa49845b436ea04d10e9/20210928185128_0.jpg"}
                }
             },
            "2": {
                "type": "mention",
                "mutability": "SEGMENTED",
                "data": {
                    "mention": {
                        "name": "funkymikky4ril",
                        "link": "funkymikky4ril@yahoo.com",
                        "avatar": "https://api.zuri.chat/files/profile_image/614679ee1a5607b13c00bcb7/6146fa49845b436ea04d10e9/20210928185128_0.jpg"}
                }
            },
            "3": {
                "type": "mention",
                "mutability": "SEGMENTED",
                "data": {
                    "mention": {
                        "name": "valenteeena", "link": "valenteeena@gmail.com", "avatar": "https://api.zuri.chat/files/profile_image/614679ee1a5607b13c00bcb7/614f06e6e35bb73a77bc2aa3/20211002190529_0.gif"}
                }
            },
            "4": {"type": "mention",
                  "mutability": "SEGMENTED",
                  "data": {
                      "mention": {
                          "name": "davidoluwatobi41",
                          "link": "davidoluwatobi41@gmail.com",
                          "avatar": "https://api.zuri.chat/files/profile_image/614679ee1a5607b13c00bcb7/614f06cbe35bb73a77bc2a94/20210928132937_0.png"
                      }
                  }
                  }
        }
    }
}


# hey = message["richUiData"]['entityMap']['0']['data']['mention']['name']


hey = message["richUiData"]['entityMap']

# print(len(hey))

for i in range(len(hey)):
    # print(hey[str(i)]['data']['mention']['name'])
    # print(hey[str(i)]['data']['mention']['link'])
    pass

import requests

async def test_endpoint():
    # async with httpx.AsyncClient as client:
    #     response = await client.get('https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio')



    response = requests.get('https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio')

    # print(response)
    # print(response.json())
    print(response)

    return response.status_code
# pprint(hey)

async def hello():
    # requests = httpx.AsyncClient()
    async with httpx.AsyncClient() as client:
        response = await client.get('https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio')


    print(response.status_code)


    return response.status_code

    # await requests.aclose()


