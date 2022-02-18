from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView

from livro.forms import LivroForm
from livro.models import Livro

class LivroUpdateView(UpdateView):
    model = Livro
    template_name = 'my-create.html'
    form_class = LivroForm
    success_url = '/livro/my-livros/'

class LivrosView(ListView):
    model = Livro
    template_name = 'my-livros.html'

class LivroCreateView(CreateView):
    model = Livro
    template_name = 'my-create.html'
    form_class = LivroForm
    success_url = '/livro/my-livros/'

class LivroDetailByIdView(DetailView):
    model = Livro
    template_name = 'my-livro-detail.html'