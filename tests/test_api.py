import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.parametrize('user_id', [1, 2, 3])
def test_get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert 'name' in response.json()
