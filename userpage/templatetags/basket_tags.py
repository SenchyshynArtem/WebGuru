from django import template
from basket.models import ProductInBasket

register = template.Library()


@register.simple_tag
def get_prods_in_basket_amount(request):
    session_key = request.session.session_key
    product_list = ProductInBasket.objects.filter(session_key=session_key)
    count = len(product_list)
    return count
