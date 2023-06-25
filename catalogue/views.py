from django.shortcuts import render, get_object_or_404
from .models import *
from basket.models import *


def show_catalogue(request):
    context = {}
    all_products = Products.objects.all()
    context['all_products'] = all_products
    return render(request, "catalogue/catalogue.html", context=context)


def show_product(request, product_pk):
    if request.method == 'POST':
        # Получаем из запроса ключ сессии пользователя 
        session_key = request.session.session_key
        # Если ключ сессии пустой
        if not session_key:
            # Сгенерировать новый ключ сессии
            request.session.cycle_key()
            # Получаем из запроса ключ сессии пользователя  
            session_key = request.session.session_key
        # Створюємо об'єкт ProductInBasket з ключем сесії та ідентифікатором продукту
        productInBasket = ProductInBasket.objects.create(session_key=session_key ,product_id=product_pk)
        # Створюємо порожній список для додаткових параметрів
        additional_parameters_list = []
        # Для кожного ідентифікатора додаткового параметра, який отриманий з запиту
        for pk in request.POST.getlist('additional-parameter-pk'):
            # Знаходимо відповідний об'єкт AdditionalParameter за ідентифікатором
            additional_parameter = AdditionalParameter.objects.get(pk=pk)
            # Додаємо його до списку додаткових параметрів
            additional_parameters_list.append(additional_parameter)
        # Встановлюємо зв'язок між об'єктом ProductInBasket та списком додаткових параметрів
        productInBasket.additional_parameters.set(additional_parameters_list)
        # Зберігаємо зміни в об'єкті ProductInBasket
        productInBasket.save()
    product = get_object_or_404(Products, pk=product_pk)
    additional_parameters = AdditionalParameter.objects.all()
    full_price = product.price
    for parameter in additional_parameters:
        full_price += parameter.price
    return render(request, "catalogue/product.html", context={'product': product, 'add_parameters': additional_parameters, 'full_price': full_price})
