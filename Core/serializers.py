from rest_framework import serializers
from Core.models import AgendaDisponivel,Agendamento

class AgendaDisponivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaDisponivel
        fields = '__all__'
        
class AgendaSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Agendamento
        fields = '__all__'
