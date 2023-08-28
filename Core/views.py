from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Pesquisa,Imoveis
from .serializers import PesquisaSerializer, ImoveisSerielizer
from rest_framework import viewsets,status
import requests


def  pesquisa(request,estado):
    r = requests.get(f'https://venda-imoveis.caixa.gov.br/listaweb/Lista_imoveis_{estado}.csv')
    context = {
        # 
    }
    return render(request,'homt.html',context)
