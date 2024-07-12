from selene import browser, have
import allure
from helpers.attach import request_with_logs


class CartPage:

    def __init__(self, product):
        self.response = request_with_logs(f"https://demowebshop.tricentis.com/addproducttocart/catalog/{product}")

    @allure.step('Открыть браузер')
    def open_shop(self):
        self.add_good_to_cart()
        browser.open('/cart')
        browser.driver.add_cookie({"name": "Nop.customer", "value": self.id_cart})
        browser.driver.refresh()

    @allure.step('Добавить товар в корзину через апи')
    def add_good_to_cart(self):
        assert self.response.status_code == 200
        self.id_cart = self.response.cookies.get("Nop.customer")

    @allure.step('Проверить товар в корзине')
    def check_cart_with_good(self):
        browser.element('.product-name').should(have.exact_text('Computing and Internet'))

    @allure.step('Проверить цену товара')
    def check_price_of_good(self):
        browser.element('.product-unit-price').should(have.exact_text('24.00'))

    @allure.step('Проверить ошибку добавления товара в корзину')
    def check_error_for_nonexistent_good(self):
        assert self.response.status_code == 404
