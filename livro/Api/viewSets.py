from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from autor.Api.serializers import AutorSerializer
from autor.models import Autor
from editora.models import Editora
from livro.Api import serializers
from livro.Api.serializers import LivroSerializer
from livro.models import Livro


class LivroViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.LivroSerializer
    queryset = Livro.objects.all()

    @action(methods=['get'], detail=False, url_path='listar_livros_por_autor')
    def list_por_autor(self,request):
            name_str = "name"
            name = request.GET.get(name_str)
            autor = Autor.objects.get(nome_autor=name)
            return Response(status=status.HTTP_200_OK, data=LivroSerializer(instance=autor.livros, many=True,
                                                                                context={'request': request}).data)

    @action(methods=['get'], detail=False, url_path='listar_livros_por_editora')
    def list_por_editora(self,request):
        name_str = "name"
        name = request.GET.get(name_str)
        editora = Editora.objects.get(nome_editora=name)
        return Response(status=status.HTTP_200_OK, data=LivroSerializer(instance=editora.livros, many=True,
                                                                        context={'request': request}).data)
