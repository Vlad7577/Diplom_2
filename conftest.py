import pytest
from helpers import create_user, delete_user
from data import generate_email, generate_password, generate_name


@pytest.fixture
def new_user():
    payload = {
        "email": generate_email(),
        "password": generate_password(),
        "name": generate_name()
    }

    response = create_user(payload)
    access_token = response.json().get("accessToken")

    yield payload, access_token

    if access_token:
        delete_user(access_token)