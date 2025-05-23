from http import HTTPStatus


def test_read_root_deve_retornar_ok(client):
    response = client.get("/")  # Act (Acao)
    assert response.json() == {"message": "Hello, world!"}  # Assert
    assert response.status_code == HTTPStatus.OK  # Assert


def test_read_batatinha_deve_retornar_uma_pagina_html_com_titulo(client):
    response = client.get("/batatinha")  # Act (Acao)
    assert response.status_code == HTTPStatus.OK  # Assert
    assert "text/html" in response.headers["content-type"]  # Assert


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "secret",
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
    }


def test_read_users(client):
    # Get the users list
    response = client.get("/users/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [{
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com",
        }]
    }
