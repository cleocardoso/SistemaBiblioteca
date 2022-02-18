from rest_framework import serializers

from livro.models import Livro


class LivroSerializer(serializers.ModelSerializer):
    class Meta:

        model = Livro
        #fields = ('nome_autor')
        fields = ('__all__')