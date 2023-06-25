from django.shortcuts import render
from django.http import HttpResponse
from basket.telegram import send_message_tg
from webguru.settings import TELEGRAM_CHAT_ID, TELEGRAM_BOT_TOKEN

# Create your views here.
def show_about_us(request):
    return render(request, "user_pages/about_us.html")

def show_main(request):
    return render(request, "user_pages/main.html")

def feedback_success(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    feedback_message = request.POST.get('feedback-message')

    message = f"Нове повідомлення.\nІм'я:{name}.\nПошта:{email}.\nВаше повідомлення:{feedback_message}."
    send_message_tg(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)
    return HttpResponse('Повідомлення надіслано')