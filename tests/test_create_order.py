import allure
from helpers import create_order


class TestCreateOrder:

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_authorized(self, new_user):
        payload, token = new_user

        ingredients = ["61c0c5a71d1f82001bdaaa6d"]

        response = create_order(token, ingredients)

        assert response.status_code == 200


    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self):

        ingredients = ["61c0c5a71d1f82001bdaaa6d"]

        response = create_order("", ingredients)

        assert response.status_code == 200


    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients(self, new_user):
        payload, token = new_user

        response = create_order(token, [])

        assert response.status_code == 400


    @allure.title("Создание заказа с ингредиентами без авторизации")
    def test_create_order_with_ingredients_no_auth(self):

        ingredients = ["61c0c5a71d1f82001bdaaa6d"]

        response = create_order("", ingredients)

        assert response.status_code == 200


    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_hash(self, new_user):
        payload, token = new_user

        ingredients = ["invalid_hash"]

        response = create_order(token, ingredients)

        assert response.status_code == 400