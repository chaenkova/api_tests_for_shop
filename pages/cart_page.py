from selene import browser, have
import allure
from helpers.attach import request_with_logs


class CartPage:

    @allure.step('Открыть браузер')
    def open_shop(self, id_customer):
        browser.open('/cart')
        browser.driver.add_cookie({"name": "Nop.customer", "value": id_customer})
        browser.driver.refresh()

    @allure.step('Добавить товар в корзину через апи')
    def add_good_to_cart(self, good):
        response = request_with_logs(f"https://demowebshop.tricentis.com/addproducttocart/catalog/{good}")
        assert response.status_code == 200
        return response.cookies.get("Nop.customer")

    @allure.step('Проверить товар в корзине')
    def check_cart_with_good(self):
        browser.element('.product-name').should(have.exact_text('Computing and Internet'))

    @allure.step('Проверить цену товара')
    def check_price_of_good(self):
        browser.element('.product-unit-price').should(have.exact_text('10.00'))

    @allure.step('Проверить ошибку добавления товара в корзину')
    def check_cart_without_good(self, good):
        response = request_with_logs(f"https://demowebshop.tricentis.com/addproducttocart/catalog/{good}")
        assert response.status_code == 404
