from rest_framework import viewsets
from autor.Api import serializers
from autor.models import Autor


class AutoresViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.AutorSerializer
    queryset = Autor.objects.all()

