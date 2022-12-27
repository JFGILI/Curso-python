
from django.http import HttpResponse
from django.shortcuts import render
from relatives.models import Relatives

def hola_mundo(request):
    return HttpResponse("Hola Mundo! primera view de prueba")

def create_relative(request):
    new_relative = Relatives.objects.create(name='Heide TOMLIENOVICH', birth=1959 , alive=True )
    print (new_relative) 
    return HttpResponse('Se creo un nuevo pariente')

def list_relatives(request):
    all_relatives = Relatives.objects.all()
    print(all_relatives)
    context={
        'relatives': all_relatives,
    }
    return render (request,'list_relatives.html', context=context)