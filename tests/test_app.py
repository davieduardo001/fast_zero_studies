from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fast_zero.app import app


def test_read_root_deve_retornar_ok():
    client = TestClient(app)  # Arrange (Organizacao)
    response = client.get("/")  # Act (Acao)
    assert response.json() == {"message": "Hello, world!"}  # Assert
    assert response.status_code == HTTPStatus.OK  # Assert


def test_read_batatinha_deve_retornar_batatinha():
    client = TestClient(app)  # Arrange (Organizacao)
    response = client.get("/batatinha")  # Act (Acao)
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {"message": "Batatinha"}  # Assert
