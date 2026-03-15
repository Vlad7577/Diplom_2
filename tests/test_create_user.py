import allure
from helpers import create_user
from data import generate_email, generate_password, generate_name


class TestCreateUser:

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self):
        payload = {
            "email": generate_email(),
            "password": generate_password(),
            "name": generate_name()
        }

        response = create_user(payload)

        assert response.status_code == 200
        assert response.json()["success"]

    @allure.title("Создание пользователя, который уже существует")
    def test_create_existing_user(self, new_user):
        payload, token = new_user

        response = create_user(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False
        assert response.json()["message"] == "User already exists"

    @allure.title("Создание пользователя без обязательного поля")
    def test_create_user_without_field(self):
        payload = {
            "email": generate_email(),
            "password": generate_password()
        }

        response = create_user(payload)

        assert response.status_code == 403
        assert response.json()["success"] is False