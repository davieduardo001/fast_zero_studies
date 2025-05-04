from fastapi import FastAPI
from http import HTTPStatus
from fast_zero.schemas import Message

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello, world!"}


@app.get("/batatinha", status_code=HTTPStatus.OK)
def read_batatatinha():
    return {"message": "Batatinha"}
