import allure
from helpers import login_user


class TestLoginUser:

    @allure.title("Логин существующего пользователя")
    def test_login_user(self, new_user):
        payload, token = new_user

        login_data = {
            "email": payload["email"],
            "password": payload["password"]
        }

        response = login_user(login_data)

        assert response.status_code == 200
        assert response.json()["success"]

    @allure.title("Логин с неверными данными")
    def test_login_wrong_user(self):

        login_data = {
            "email": "wrong@email.com",
            "password": "123456"
        }

        response = login_user(login_data)

        assert response.status_code == 401
        assert not response.json()["success"]