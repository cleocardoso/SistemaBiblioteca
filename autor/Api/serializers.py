from rest_framework import serializers
from autor.models import Autor


class AutorSerializer(serializers.ModelSerializer):
    class Meta:

        model = Autor
        #fields = ('nome_autor')
        fields = ('__all__')