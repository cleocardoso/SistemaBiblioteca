from django.forms import ModelForm

from livro.models import Livro


class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = ['nome_livro', 'ano_lancamento']