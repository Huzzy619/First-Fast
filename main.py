from fastapi import FastAPI



app = FastAPI()


@app.get("/")
async def index():
    bio = "I am a Python programmer, I use Django, FastAPI and Django RestFramework for Backend Web development "
    return {
        "slackUsername": "Huzzy-K",
        "backend": True,
        "age": 24,
        "bio": bio 
        }
