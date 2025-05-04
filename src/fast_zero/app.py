from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/batatinha")
def read_batatatinha():
    return {"message": "Batatinha"}
