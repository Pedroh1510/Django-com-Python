from django.shortcuts import render, HttpResponse

# Create your views here.
def defalt_url(requests):
    return HttpResponse('Home page')
def hello(requests,name='world'):
    return HttpResponse(f'Hello {name}')
def soma(requests,x,y):
    return HttpResponse(f'{x}+{y}={x+y}')
def subtracao(requests,x,y):
    return HttpResponse(f'{x}-{y}={x-y}')
def divisao(requests,x,y):
    return HttpResponse(f'{x}/{y}={x/y}')
def multiplicacao(requests,x,y):
    return HttpResponse(f'{x}*{y}={x*y}')