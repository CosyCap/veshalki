from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),  # URL для представления index
    path('contacts/', views.contacts, name='contacts')  
]
