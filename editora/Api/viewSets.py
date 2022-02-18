from rest_framework import viewsets
from editora.Api import serializers

from editora.models import Editora


class EditorasViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.EditoraSerializer
    queryset = Editora.objects.all()