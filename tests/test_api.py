import pytest
import requests
import allure


BASE_URL = "https://jsonplaceholder.typicode.com"


@allure.title("Тест на получение всех пользователей через API")
def test_get_all_users():
    """
    Тестируем получение всех пользователей через API.
    """
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert len(response.json()) > 0


@pytest.mark.parametrize("user_id", [1, 2, 3])
@allure.title("Тест на получение пользователя по ID через API")
def test_get_user_by_id(user_id):
    """
    Тестируем получение пользователя по его ID через API.
    """
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id


@allure.title("Тест на создание поста через API")
def test_create_post():
    """
    Тестируем создание нового поста через API.
    """
    payload = {"title": "Тестовый пост", "body": "Тестовое содержание", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == payload["title"]


@allure.title("Тест на удаление поста через API")
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_post(post_id):
    """
    Тестируем удаление поста через API.
    """
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200


