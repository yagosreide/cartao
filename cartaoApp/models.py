from django.db import models

#class Agencia(models.Model):
#    id_agencia = models.AutoField(primary_key=True)
#    nome_agencia = models.CharField(max_length=255)
#    num_agencia = models.CharField(max_length=255)
    
#class Funcao(models.Model):
 #   id_funcao = models.AutoField(primary_key=True)
  #  nome_funcao = models.CharField(max_length=255)
    
#class Cartao(models.Model):
#   id_cartao = models.AutoField(primary_key=True)
#   banco_cartao = models.CharField(max_length=255,null=False) 
#  num_cartao = models.CharField(max_length=255,null=False) 
#    cliente_cartao = models.CharField(max_length=255,null=False) 
#   venc_cartao = models.CharField(max_length=255,null=False)
#    cv_cartao = models.CharField(max_length=255,null=False) 
#    id_agencia = models.ForeignKey(Agencia,models.DO_NOTHING,db_column='id_agencia') 
#    id_funcao = models.ForeignKey(Funcao,models.DO_NOTHING,db_column='id_funcao')

class Validar(models.Model):
    id_validar = models.AutoField(primary_key=True)
    cartao_validar = models.CharField(max_length=255, null=False)
    cpf_validar = models.CharField(max_length=255, null=False)
    nome_validar = models.CharField(max_length=255, null=False)
    codigo_validar = models.CharField(max_length=255, null=False)
    data_validar =  models.CharField(max_length=255, null=False)
    