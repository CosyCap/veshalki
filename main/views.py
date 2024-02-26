from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contacts
from django.contrib import messages 
from django.core.mail import send_mail 

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
        
        if name and email and question:
            message = f'От: {name}\nEmail: {email}\nТелефон: {phone_number}\n\nВопрос:\n{question}'
            send_mail(
                'Новый вопрос от посетителя вашего сайта',
                message,
                email,
                ['your_email@example.com'],  
                fail_silently=False,
            )
            
            Contacts.objects.create(name=name, email=email, phone_number=phone_number, question=question)
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')
            return redirect('/') 
        else:
            error_message = 'Пожалуйста, заполните все обязательные поля.'
            context = {'error_message': error_message,}
            return render(request, 'main/contacts.html', context)
    else:
        error_message = 'Пожалуйста, заполните все обязательные поля.'
        title = 'Контакты'  # Устанавливаем заголовок страницы
        context = {'error_message': error_message, 'title': title}
        return render(request, 'main/contacts.html', context)
    
def handler404(request, exception):
    return render(request, 'main/pages-404.html', status=404)

    