
# Project Title

A brief description of what this project does and who it's for


## Run Locally


Install dependencies

```bash
  pip install fastapi "uvicorn[standard]"
```

To run directly 

```bash
  python dataclass.py
```


## Documentation

[Documentation](https://linktodocumentation)

To use the DataClass from the dataclass module 
```bash
from dataclass import DataClass
```

Structure
```bash
data = DataClass(
    
    [
        # Data Sources
        [ {}, {} ],  # Celebrity API
        [ {}, {} ],   # Twitter API
        [ {}, {} ],   #LinkedIn
        ...
    ] 
  )
```

Note: it has to be a List of list(Data source) of Dictionaries(profiles)

Optionally: Any of these "Keyword arguments" can be passed to help filter the results better, 'name' is required
```bash
            data = DataClass(

                [
                    # Data Sources
                    [ {}, {} ],  # Celebrity API
                    [ {}, {} ],   # Twitter API
                    [ {}, {} ],   #LinkedIn
                    ...
                ],

                name = "john doe", # required
                age = 23,
                occupation = "banker",
                gender = 'male',

                )
```


A very important thing to note is that the DataClass expects the dictionaries to have all of these keys.
So even if there's no value for it, just return the key and value as None.

Secondly, You can pass the occupation as a string or a List(if multiple). The DataClass will handle the complications

Example:

    # Celebrity API

    [
        {
            "name": "elon musk",
            "age": 51,
            "gender": "male",
            "occupation": [

                    "film_producer",
                    "engineer",
            ],
            "vip_score": 8.75,
        },

        {
            "name": "barack obama",
            "age": None,
            "gender": None,
            "occupation": "politics",
            "vip_score": 3,
        },
    ]



Finally, to execute the Dataclass:

response = data.initiate()


This will return unique profile(s) gotten from all sources.

Please reach out to me (@Huzzy-K or @Tech Matt) in case of any further complications
