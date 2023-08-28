from django.db import models


class Pesquisa(models.Model):
    Estado = models.CharField(max_length=2)

class Imoveis(models.Model):
    NUMERO_IMOVEL = models.CharField(max_length=20, blank=False)
    UF = models.CharField(max_length=2 , blank=False)
    CIDADE = models.CharField(max_length=50, blank=False)
    BAIRRO = models.CharField(max_length=50, blank=False)
    ENDERECO = models.CharField(max_length=100, blank=False)
    PRECO = models.FloatField(blank=False)
    VALOR_AVALIACAO = models.FloatField(blank=False)
    DESCONTO = models.DecimalField
    DESCRICAO = models.CharField(max_length=100,blank=False)
    MODALIDADE_VENDA = models.CharField(max_length=20 , blank=False)
    LINK_ACESSO = models.CharField(max_length=150 , blank=False)