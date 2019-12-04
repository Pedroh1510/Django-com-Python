from django.shortcuts import render, HttpResponse, redirect
from core.models import Eventos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import Http404
from datetime import datetime, timedelta

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
    dataAtual = datetime.now()- timedelta(hours=1)
    eventos = Eventos.objects.filter(usuario=user, dataEvento__gt=dataAtual)
    dados = {'eventos':eventos}
    return render(request,'agenda.html',dados)

@login_required(login_url='/login/')
def evento(request):
    idEvento = request.GET.get('id')
    dados={}
    if idEvento:
        dados['evento'] = Eventos.objects.get(id=idEvento)
    return render(request,'evento.html',dados)

@login_required(login_url='/login/')
def submitEvento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        dataEvento = request.POST.get('dataEvento')
        descricao = request.POST.get('descricao')
        local = request.POST.get('local')
        idEvento = request.POST.get('idEvento')
        usuario = request.user
        if idEvento:
            evento = Eventos.objects.get(id=idEvento)
            if evento.usuario==usuario:
                evento.titulo=titulo
                evento.dataEvento=dataEvento
                evento.descricao=descricao
                evento.local=local
                evento.save()
        else:
            Eventos.objects.create(titulo= titulo,dataEvento=dataEvento,descricao=descricao,usuario=usuario,local=local)
    return redirect('/')

@login_required(login_url='/login/')
def deleteEvento(request,idEvento):
    try:
        evento = Eventos.objects.get(id=idEvento)
    except Exception:
        Http404
    if request.user == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')
