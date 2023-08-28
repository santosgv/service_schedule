from rest_framework import serializers
from Core.models import Pesquisa, Imoveis

class PesquisaSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Pesquisa
        fields = '__all__'
        
class ImoveisSerielizer(serializers.ModelSerializer):
    class Meta:
        model = Imoveis
        fields = '__all__'
