import allure
import logging
import json
from allure_commons.types import AttachmentType
import requests
from selene import browser, have


@allure.step('Открыть браузер')
def open_shop(id_customer):
    browser.open('/cart')
    browser.driver.add_cookie({"name": "Nop.customer", "value": id_customer})
    browser.driver.refresh()


@allure.step('Добавить товар в корзину через апи')
def add_good_to_cart(good):
    response = request_with_logs(f"https://demowebshop.tricentis.com/addproducttocart/catalog/{good}")
    assert response.status_code == 200
    return response.cookies.get("Nop.customer")


def request_with_logs(url):
    response = requests.post(url)
    if response.request.body:
        allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Response",
                      attachment_type=AttachmentType.JSON, extension="json")
    allure.attach(body=str(response.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
    logging.info(response.request.url)
    logging.info(response.status_code)
    logging.info(response.text)
    return response


@allure.step('Проверить товар в корзине')
def check_cart_with_good():
    browser.element('.product-name').should(have.exact_text('Computing and Internet'))


@allure.step('Проверить ошибку добавления товара в корзину')
def check_cart_without_good(good):
    response = request_with_logs(f"https://demowebshop.tricentis.com/addproducttocart/catalog/{good}")
    assert response.status_code == 404


@allure.feature("Добавление товаров в корзину")
@allure.title("Проверка добавления в корзину несуществующего товара")
def test_wrong_good_add_to_cart():
    check_cart_without_good("10000")


@allure.feature("Добавление товаров в корзину")
@allure.title("Проверка добавления в корзину существующего товара")
@allure.link('https://demowebshop.tricentis.com/cart', name='Корзина')
def test_success_add_good_to_cart():
    id_cart = add_good_to_cart("13/1/1")
    open_shop(id_cart)
    check_cart_with_good()
