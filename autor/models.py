from django.db import models

from livro.models import Livro


class Autor(models.Model):
    nome_autor = models.CharField('nome_autor', max_length=255)
    livros = models.ManyToManyField(Livro, related_name='Livro')

    def __str__(self):
        return str(self.nome_autor)

    class Meta:
        db_table = 'autor'