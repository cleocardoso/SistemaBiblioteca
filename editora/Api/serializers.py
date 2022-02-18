from rest_framework import serializers

from editora.models import Editora


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:

        model = Editora
        #fields = ('nome_autor')
        fields = ('__all__')