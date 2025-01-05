shopping_cart = {}


def add_product(product_name: str, price: float, quantity: int) -> None:
    """
    Add a product to the shopping cart.
    :param product_name: name
    :param price: price
    :param quantity: quantity
    """
    if product_name in shopping_cart.keys():
        product = shopping_cart[product_name]
        product.quantity += quantity
    else:
        shopping_cart[product_name] = {
            'price': price,
            'quantity': quantity
        }


def remove_product(product_name: str):
    """
    Remove a product from the shopping cart.
    :param product_name: name
    """
    if product_name in shopping_cart.keys():
        shopping_cart.pop(product_name)
    else:
        print('Product not in cart.')


def update_quantity(product_name: str, quantity: int):
    """
    Update the quantity of a product from the shopping cart.
    :param product_name: name
    :param quantity: quantity
    """
    if product_name in shopping_cart.keys():
        shopping_cart[product_name]['quantity'] = quantity
    else:
        print('Product not in cart.')


def calculate_total_price() -> float:
    """
    Calculate the total price of the shopping cart.
    :return: total price of the shopping cart.
    """
    total_price = 0
    for key, value in shopping_cart.items():
        total_price += value['price'] * value['quantity']
    return total_price


def checkout():
    """
    Checkout the shopping cart.
    """
    print('已结算购物车，商品总价为: ', calculate_total_price())
    shopping_cart.clear()


if __name__ == '__main__':
    add_product("Apple", 2.5, 3)
    add_product("Banana", 1.5, 2)
    add_product("Orange", 3.0, 1)

    print("当前购物车：", shopping_cart)
    print("当前购物车商品总价值:", calculate_total_price())

    remove_product("Banana")
    update_quantity("Apple", 5)

    print("更新后购物车：", shopping_cart)
    print("更新后购物车商品总价值:", calculate_total_price())

    checkout()
    print("结算后购物车：", shopping_cart)
