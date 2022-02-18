from django.contrib import admin

# Register your models here.
import livro
from livro.models import Livro

class MyModelAdmin(admin.ModelAdmin):
   list_display = ['nome_livro','ano_lancamento']
   search_fields= ['nome_livro','ano_lancamento']
   list_filter = ['nome_livro','ano_lancamento']


admin.site.register(Livro, MyModelAdmin)