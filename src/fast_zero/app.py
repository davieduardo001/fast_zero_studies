from http import HTTPStatus
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from fast_zero.schemas import Message

app = FastAPI()

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent

# Mount static files
app.mount(
    "/static",
    StaticFiles(directory=str(PROJECT_ROOT / "static")),
    name="static",
)


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello, world!"}


@app.get("/batatinha", status_code=HTTPStatus.OK)
def read_batatatinha():
    return FileResponse(PROJECT_ROOT / "static" / "batatinha.html")
