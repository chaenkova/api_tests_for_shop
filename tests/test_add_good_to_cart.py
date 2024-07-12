import allure
from pages.cart_page import CartPage
from selene import browser, have


@allure.feature("Добавление товаров в корзину")
@allure.title("Проверка добавления в корзину несуществующего товара")
def test_wrong_good_add_to_cart():
    CartPage("10000").check_error_for_nonexistent_good()


@allure.feature("Добавление товаров в корзину")
@allure.title("Проверка добавления в корзину существующего товара")
@allure.link('https://demowebshop.tricentis.com/cart', name='Корзина')
def test_success_add_good_to_cart(browser_settings):
    cart = CartPage("13/1/1")
    cart.open_shop()
    cart.check_cart_with_good()


@allure.title("Проверка стоимости добавленного товара")
@allure.link('https://demowebshop.tricentis.com/cart', name='Корзина')
def test_check_price_of_good_in_cart(browser_settings):
    cart = CartPage("45/1/1")
    cart.open_shop()
    cart.check_price_of_good()
