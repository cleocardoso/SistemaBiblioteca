from django.contrib import admin

# Register your models here.
from autor.models import Autor


class MyModelAdmin(admin.ModelAdmin):
   list_display = ['nome_autor']
   search_fields= ['nome_autor', 'livros']
   list_filter = ['nome_autor', 'livros']


admin.site.register(Autor, MyModelAdmin)