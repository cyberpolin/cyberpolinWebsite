from rest_framework import serializers
from articulos.models import *


class Post(serializers.ModelSerializer):
	class Meta:
		model = Publicacion
		fields = ('titulo', 'texto', 'tipo', 'fecha')