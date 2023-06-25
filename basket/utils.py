def counted_full_price(products_in_basket):
    full_price = 0
    # Перебор products_in_basket
    for prod_in_basket in products_in_basket:
        # Обновление переменной final_price, добавляя к ней цену за каждый продукт в корзине
        full_price += prod_in_basket.product.price
        # Перебор prod_in_basket.additional_parameters
        for additional_param in prod_in_basket.additional_parameters.all():
            # Обновление переменной final_price, добавляя к ней цену за каждый доп. параметр, если такие имеются в заказе
            full_price += additional_param.price
    return full_price