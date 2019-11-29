from django.shortcuts import render, HttpResponse

# Create your views here.
def defalt_url(requests):
    return HttpResponse('Home page')
def hello(requests,name='world'):
    return HttpResponse(f'Hello {name}')