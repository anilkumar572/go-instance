from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello World"}


@app.get("/hello")
def hello_endpoint():
    return {"message": "Hello World"}
