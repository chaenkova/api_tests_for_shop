import allure
from pages.cart_page import CartPage
from selene import browser, have


@allure.feature("Добавление товаров в корзину")
@allure.title("Проверка добавления в корзину несуществующего товара")
def test_wrong_good_add_to_cart():
    CartPage().check_cart_without_good("10000")


@allure.feature("Добавление товаров в корзину")
@allure.title("Проверка добавления в корзину существующего товара")
@allure.link('https://demowebshop.tricentis.com/cart', name='Корзина')
def test_success_add_good_to_cart():
    cart = CartPage()
    id_cart = cart.add_good_to_cart("13/1/1")
    cart.open_shop(id_cart)
    cart.check_cart_with_good()


@allure.title("Проверка стоимости добавленного товара")
@allure.link('https://demowebshop.tricentis.com/cart', name='Корзина')
def test_success_remove_good_to_cart():
    cart = CartPage()
    id_cart = cart.add_good_to_cart("13/1/1")
    cart.open_shop(id_cart)
    cart.check_price_of_good()
