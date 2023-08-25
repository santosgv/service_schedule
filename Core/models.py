from django.db import models

from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    # Outros campos relacionados ao serviço

class Agendamento(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    # Outros campos relacionados ao agendamento

    class Meta:
        unique_together = ['data', 'hora']  # Impede agendamentos duplicados

class AgendaDisponivel(models.Model):
    data = models.DateField()
    horarios_disponiveis = models.ManyToManyField('HorarioDisponivel')

class HorarioDisponivel(models.Model):
    hora = models.TimeField()
    disponivel = models.BooleanField(default=True)
