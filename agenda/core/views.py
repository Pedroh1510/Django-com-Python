from django.shortcuts import render, HttpResponse, redirect
from core.models import Eventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def loginUser(request):
    return render(request,'login.html')

def submitLogin(request):
    if request.POST:
        user = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=user,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,'Usuário e/ou senha inválidos')
    return redirect('/')

def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/login/')
def listaEventos(request):
    user = request.user
    eventos = Eventos.objects.filter(usuario=user)
    dados = {'eventos':eventos}
    return render(request,'agenda.html',dados)

@login_required(login_url='/login/')
def evento(request):
    return render(request,'evento.html')

@login_required(login_url='/login/')
def submitEvento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        dataEvento = request.POST.get('dataEvento')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        usuario = request.user
        Eventos.objects.create(titulo= titulo,dataEvento=dataEvento,descricao=descricao,usuario=usuario,local=local)
    return redirect('/')

@login_required(login_url='/login/')
def eventoLocal(request,evento):
    eventoObject = Eventos.objects.get(titulo=evento)
    page= []
    page.append(f'<li>Descrição do evento: {eventoObject.usuario}</li>')
    page.append(f'<li>Descrição do evento: {eventoObject.descricao}</li>')
    page.append(f'<li>Data do evento: {eventoObject.dataEvento}</li>')
    page.append(f'<li>Local do evento: {eventoObject.local}</li>')
    return HttpResponse(page)