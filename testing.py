
import json

hey =      {
            # "name": "barack obama",
            "age": 12,
            "gender": "male",
            "occupation": "politics",
            # "vip_score": 3,
        },

hi =     {
            # "name": "Bar Obama",
            "age": 12,
            "gender": "male",
            "occupation": "politics",
            # "vip_score": 8,
        },
        


hey = json.dumps(hey)
hi = json.dumps(hi)

print({hey} | {hi})


