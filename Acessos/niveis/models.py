#coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError
import datetime

# Create your models here.

Acesso = [
     ('1','LIVRE'),
     ('2','RESTRITO'),
     ('3','RESERVADO')
] 

#class Acesso (models.Model):
	#Descricao = models.CharField('Tipo de Acesso',max_length=100,null=True)
	
	#def __unicode__(self):
		#return self.Descricao


class Pessoa (models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	Endereco = models.CharField('Endereço',max_length=100,null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True)
	Descricao = models.CharField('Acesso',max_length=1,choices=Acesso,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Nome,self.Descricao)
	
class Lugar (models.Model):
	Nome = models.CharField('Lugar',max_length=100,null=True)
	Descricao = models.CharField('Acesso',max_length=1,choices=Acesso,null=True)
	
	def __unicode__(self):
		return "%s - %s" % (self.Nome,self.Descricao)
		
class validacao (models.Model):
	Nome = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Local = models.ForeignKey(Lugar,verbose_name="Local",null=True)
	Entrada = models.TimeField(auto_now=True,null=True)
	Saida = models.TimeField(auto_now=False,null=True)
	
	def clean(self):
		if (self.Nome.Descricao == '1' and self.Local.Descricao == '2'):
			raise ValidationError("Pessoa não tem acesso a esta area")
		if (self.Nome.Descricao == '1' and self.Local.Descricao == '3'):
			raise ValidationError("Pessoa não tem acesso a esta area")
		if (self.Nome.Descricao == '2' and self.Local.Descricao == '3'):
			raise ValidationError("Pessoa não tem acesso a esta area")
		if (self.Entrada == self.Saida):
			raise ValidationError("Horario Inadequado")
		if (self.Entrada > self.Saida):
			raise ValidationError("Horario Inadequado")

			
		q = validacao.objects.filter(Nome=self.Nome,Saida__isnull=True)
		if q and self.id == None:
			raise ValidationError("Pessoa em outro evento")
	
	#def clean(self):
		#q = validacao.objects.filter(Nome=self.Nome.Descricao,Local=self.Descricao)
		
		#if not q:
			#raise ValidationError("Pessoa não tem acesso a esta area")
			
	#def clean(self):
		#q = validacao.objects.filter(Entrada!=self.Saida)
		
		#if not q:
			#raise ValidationError("Horario Inadequado")
		
	#class Meta:
		#unique_together = ("Nome","Local")
	

