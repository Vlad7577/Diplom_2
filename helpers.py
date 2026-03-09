import requests

BASE_URL = "https://stellarburgers.education-services.ru/api"


def create_user(data):
    return requests.post(f"{BASE_URL}/auth/register", json=data)


def login_user(data):
    return requests.post(f"{BASE_URL}/auth/login", json=data)


def delete_user(token):
    headers = {"Authorization": token}
    return requests.delete(f"{BASE_URL}/auth/user", headers=headers)


def create_order(token, ingredients):
    headers = {"Authorization": token}
    data = {"ingredients": ingredients}
    return requests.post(f"{BASE_URL}/orders", json=data, headers=headers)