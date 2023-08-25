from django.contrib import admin
from models import Servico,Agendamento,AgendaDisponivel,HorarioDisponivel

admin.site.register(Servico)
admin.site.register(Agendamento)
admin.site.register(AgendaDisponivel)
admin.site.register(HorarioDisponivel)