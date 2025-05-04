from http import HTTPStatus
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from fast_zero.schemas import (
    Message,
    UserDB,
    UserList,
    UserPublicSchema,
    UserSchema,
)

app = FastAPI()

database = []

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


@app.post(
    "/users/", response_model=UserPublicSchema, status_code=HTTPStatus.CREATED
)
def create_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())

    database.append(user_with_id)

    return user_with_id


@app.get("/users/", response_model=UserList)
def read_users():
    # Convert UserDB objects to UserPublicSchema
    public_users = [
        UserPublicSchema(
            id=user.id,
            name=user.name,
            email=user.email
        )
        for user in database
    ]
    return UserList(users=public_users)
