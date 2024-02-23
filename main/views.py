from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacts
from django.contrib import messages  # Импортируем messages для работы с сообщениями обратной связи


def index(request):
    context = {
        'title': 'Металлические напольные вешалки для одежды', 
    }
    return render(request, 'main/index.html', context)

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        question = request.POST.get('question')
        if name:
            Contacts.objects.create(name=name, email=email, phone_number=phone_number, question=question)
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')  # Сохраняем сообщение об успешной отправке в объекте messages
            return redirect('/') 
        else:
            error_message = 'Вы забыли указать имя'
            context = {'error_message': error_message}
            return render(request, 'main/index.html', context)
    else:
        context = {}
        return render(request, 'main/contacts.html', context)