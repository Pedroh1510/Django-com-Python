from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eventos(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    dataEvento = models.DateTimeField(verbose_name='Data do Evento')
    dataCriacao = models.DateTimeField(auto_now=True,verbose_name='Data de Criação')
    local = models.CharField(max_length=100,verbose_name='Local', null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo

    def getDataEvento(self):
        return self.dataEvento.strftime('%d/%m/%Y ás %H:%M')
    
    def getDataInputEvento(self):
        return self.dataEvento.strftime('%Y-%m-%dT%H:%M')