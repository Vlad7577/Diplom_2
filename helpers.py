import requests
import allure

BASE_URL = "https://stellarburgers.education-services.ru/api"


@allure.step("Создание пользователя")
def create_user(data):
    return requests.post(f"{BASE_URL}/auth/register", json=data)


@allure.step("Логин пользователя")
def login_user(data):
    return requests.post(f"{BASE_URL}/auth/login", json=data)


@allure.step("Удаление пользователя")
def delete_user(token):
    headers = {"Authorization": token}
    return requests.delete(f"{BASE_URL}/auth/user", headers=headers)


@allure.step("Создание заказа")
def create_order(token, ingredients):
    headers = {"Authorization": token}
    data = {"ingredients": ingredients}
    return requests.post(f"{BASE_URL}/orders", json=data, headers=headers)