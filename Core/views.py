from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import AgendaDisponivel,Agendamento
from .serializers import AgendaDisponivelSerializer, AgendaSerielizer
from rest_framework import viewsets,status

class agenda(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendaSerielizer