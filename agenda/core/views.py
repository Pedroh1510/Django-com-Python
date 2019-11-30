from django.shortcuts import render, HttpResponse
from core.models import Eventos

# Create your views here.
def eventoLocal(requests,evento):
    eventoObject = Eventos.objects.get(titulo=evento)
    page= []
    page.append(f'<li>Descrição do evento: {eventoObject.usuario}</li>')
    page.append(f'<li>Descrição do evento: {eventoObject.descricao}</li>')
    page.append(f'<li>Data do evento: {eventoObject.dataEvento}</li>')
    page.append(f'<li>Local do evento: {eventoObject.local}</li>')
    return HttpResponse(page)