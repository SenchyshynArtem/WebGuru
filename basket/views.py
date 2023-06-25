from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import ProductInBasket
from catalogue.models import AdditionalParameter
from .telegram import send_message_tg
from webguru.settings import TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN
from .utils import counted_full_price
# Create your views here.


def show_basket(request):
    if request.method == 'POST':
        session_key = request.session.session_key
        product_in_basket = ProductInBasket.objects.get(pk = request.POST.get('productPk'))
        additional_parameters = AdditionalParameter.objects.get(pk = request.POST.get('parameterPk'))

        if request.POST.get('check') == 'uncheck':
            # print(product_in_basket.additional_parameters.get(additional_parameters))


            product_in_basket.additional_parameters.remove(additional_parameters)
            product_in_basket.save()
           
        elif request.POST.get('check') == 'check':
            product_in_basket.additional_parameters.add(additional_parameters)
            product_in_basket.save()

    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(
        session_key=session_key)
    full_price = 0
    for prod_in_basket in products_in_basket:
        full_price += prod_in_basket.product.price
        for additional_param in prod_in_basket.additional_parameters.all():
            full_price += additional_param.price

    context = {'products_in_basket': products_in_basket,
               'additional_parameters': AdditionalParameter.objects.all(),
               'full_price': full_price}

    return render(request, "basket/basket.html", context)


def order_processing(request):
    # Запрос на получение данных: name, email, design, functional, comment с формы
    name = request.POST.get('name')
    email = request.POST.get('email')
    design = request.POST.get('design')
    functional = request.POST.get('functional')
    comment = request.POST.get('comment')
    # Ключ сессии пользователя
    session_key = request.session.session_key
    # Фильтрация объектов класса ProductInBasket по session_key
    products_in_basket = ProductInBasket.objects.filter(session_key = session_key)
    # Создание переменной user_order (Заказ пользователя), которая в будущем будет изменится
    user_order = ''
    # Перебор продуктов которые находятся в корзине
    for product_index, product_in_basket in enumerate(products_in_basket):
        # Добавление f строки с именем продукта, который находится в корзине у пользователя
        user_order += f'{product_in_basket.product.name}(додатково: '
        # Перебор всех дополнительных параметров продуктов, которые находятся в корзине
        for param_index, additional_parameter in  enumerate(product_in_basket.additional_parameters.all()):
            # Добавление названия доп. параметра каждого из продуктов, если такие имеются в заказе
            user_order += additional_parameter.name
            # Если доп. параметр не последний в списке, то после него ставится запятая
            if len(product_in_basket.additional_parameters.all())-1 != param_index:
                user_order += ', '
        # Если продукт не последний в списке, то после него ставится закрытая скобка и точка с запятой
        if len(products_in_basket)-1 != product_index:       
            user_order += '); '
        # Иначе - просто закрытая скобка
        else:
            user_order += ')'
    full_price = counted_full_price(products_in_basket)


    # Текст сообщения, который отправляет телеграм-бот
    message = f"Нове замовлення.\nІм'я:{name}.\nПошта:{email}.\nЗамовлення:{user_order}.\nДизайн:{design}.\nФункціонал:{functional}.\nКоментар:{comment}.\nЦіна: {full_price}$."
    ProductInBasket.objects.all().delete()
    # Вызов функции отправки сообщения телеграм-ботом
    send_message_tg(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)
    #
    return JsonResponse({})


def delete_from_basket(request):
    ProductInBasket.objects.get(pk=request.POST.get('pk_product')).delete()
    session_key = request.session.session_key
    products_in_basket = ProductInBasket.objects.filter(session_key = session_key)
    amount_product = len(products_in_basket)
    full_price = counted_full_price(products_in_basket)
    return JsonResponse({'full_price':full_price, 'amount_product':amount_product})
