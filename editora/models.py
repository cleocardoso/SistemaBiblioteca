from django.db import models

from livro.models import Livro


class Editora(models.Model):
    nome_editora = models.CharField('nome_editora', max_length=255)
    livros = models.ManyToManyField(Livro, related_name='livro')

    def __str__(self):
        return str(self.nome_editora)

    class Meta:
        db_table = 'editora'