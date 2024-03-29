from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),  
    path('contacts/', views.contacts, name='contacts')  
]


handler404 = 'main.views.handler404'