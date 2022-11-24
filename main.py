from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re
from source import celebrity_api2
from dataclass import DataClass
from tech_matt import vip_calc

app = FastAPI()


class Arithmetic(BaseModel):

    x: int
    y: int
    operation_type: str


@app.get('/')
def index():
    return {
        'Hello': 'Welcome to My first fast'
    }


@app.post('/evaluate')
def calculate(arit: Arithmetic):

    if arit.operation_type in ['addition', '+', 'sum', 'add']:
        result = arit.x + arit.y

    elif arit.operation_type in ['subtraction', '-', 'minus', 'sub']:
        result = arit.x - arit.y

    elif arit.operation_type in ['multiplication', '*', 'times', 'mul', 'multiply']:
        result = arit.x * arit.y

    else:
        answer = solve_quiz(arit.operation_type, arit.x, arit.y)

        if answer is None:
            raise HTTPException(
                status_code=400, detail="No operation type was defined or stated")

        result = answer[0]
        arit.operation_type = answer[1]

    return {
        "slackUsername": "Huzzy-K",
        "result": result,
        "operation_type": arit.operation_type
    }


def solve_quiz(text, first, second):

    # regular expression to find numbers in a text/string
    numbers = re.findall(r'-?\d+\.?\d*', text)

    if numbers:
        x = numbers[0]
        y = numbers[1]

        # conditional type casting using tenary operator
        x = int(x) if x.isdecimal() else float(x)
        y = int(y) if y.isdecimal() else float(y)

    else:
        x = first
        y = second

    # regular expression to find operation type
    regex = re.compile(r'add|sum|sub|minus|mul|times')
    op = regex.search(text)  # The first result is used as the operator

    if op:
        operation_type = op.group()

    # if operation_type:

        if operation_type in ['add', 'sum']:

            solve = x + y
            operation = "addition"

        elif operation_type in ['sub', 'minus']:

            solve = max(x, y) - min(x, y)
            operation = "subtraction"

        elif operation_type in ['mul', 'times', 'multiply']:

            solve = x * y
            operation = "multiplication"

        return [solve, operation]

    return None


@app.get("/scrape")
def scrape_something():

    from .scrape import get_names

    get_names()
    return {
        "ok": True
    }


@app.get("/search/{name}")
def process_class(name: str):

    # Source classes
    # data1 = celebrity_api2(name)  # celebrity API
    # data2 = celebrity_api2(name)  # Twitter API
    # data3 = celebrity_api2(name)  # LinkedIn API
    # data4 = celebrity_api2(name)

    data1 = [
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
            "name": "Elon musk",
            "age": 53,
            "gender": "male",
            "occupation": [

                    "film_producer",
                    "engineer",
            ],
            "vip_score": 20.75,
        },
        {
            "name": "musa camoru",
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
            "age": 12,
            "gender": "Male",
            "occupation": "politics",
            "vip_score": 3,
        },

        {
            "name": "cole Obama",
            "age": 14,
            "gender": "male",
            "occupation": "politics",
            "vip_score": 8,
        },
    ]

    data2 = [
        {
            "name": "barack obama",
            "age": 12,
            "gender": "Male",
            "occupation": "politics",
            "vip_score": 3,
        },
    ]

    obj = DataClass([data1, data2], name=name)  # dataclass

    final_response = obj.initiate()

    return final_response


@app.get("/search2/{name}")
def process_class(name: str):

    # Source classes
    # data1 = celebrity_api2(name)  # celebrity API
    # data2 = celebrity_api2(name)  # Twitter API
    # data3 = celebrity_api2(name)  # LinkedIn API
    # data4 = celebrity_api2(name)

    from processing import Process
    from forbes import vip

    process = Process({"name": name})

    # [[{},{}]]

    # obj = DataClass([data1])

    # final_response = obj.initiate()

    return process.main()

import asyncio

@app.get('/run')
async def run():
    from NovuPy.subscribers import Subscribers
    from NovuPy.events import Events
    from NovuPy.feed import Feed
    # from NovuPy.settings import check

    ak = Subscribers()
    event = Events()

    messages = await event.get_messages()
    subscribers = await Subscribers().identify(user_id='637dbdf22610c8737861dfdf')

    print(messages)
    
    from testing import test_endpoint, hello
    import asyncio

    

    # here = asyncio.run( test_endpoint())
    # here = asyncio.run(hello())
    # here = await hello()


    # print(here)

    return {

        'hey': '1',
        'code': 'here',
        # 'url': check.base_url
        'subscriber': subscribers

    }
