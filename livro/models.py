from django.db import models


class Livro(models.Model):
    nome_livro = models.CharField('nome_livro',max_length=255)
    ano_lancamento = models.CharField('ano_lancamento', max_length=20)
    #autor = models.ManyToManyField(Autor, name='autor',related_name='autor')
    #editora = models.ForeignKey(Editora, models.CASCADE, name='editora', related_name='editora')

    def __str__(self):
        return str(self.nome_livro)

    class Meta:
        db_table = 'livro'