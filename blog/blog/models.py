from django.db import models

class tipo(models.Model):
	tipo = models.CharField
		

class Publicacion(models.Model):
	texto =  models.TextField()
	tipo = models.ForeignKey (tipo, default=0)