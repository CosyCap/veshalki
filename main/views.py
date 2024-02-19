from django.shortcuts import render

def index(request):

    context = {
        'title': 'Металлические напольные вешалки для одежды', #Потом поменяй 
    }

    return render(request, 'main/index.html', context)