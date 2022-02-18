from django.conf.urls import url
from django.urls import path, include
from livro.views import LivroDetailByIdView, LivroCreateView, LivrosView, LivroUpdateView
app_name = 'livro'

urlpatterns = [
   url(r'^my-livros/', LivrosView.as_view(), name='list-livro'),
   url(r'^livro-detail-by-id/(?P<pk>[-\w]+)',
       LivroDetailByIdView.as_view(), name='detalhe-livro'),
    url(r'^livro-update-by-id/(?P<pk>[-\w]+)',
       LivroUpdateView.as_view(), name='detalhe-livro'),
   url(r'^livro-create$', LivroCreateView.as_view()),
]