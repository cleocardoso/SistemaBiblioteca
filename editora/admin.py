from django.contrib import admin

# Register your models here.
from editora.models import Editora


class MyModelAdmin(admin.ModelAdmin):
   list_display = ['nome_editora']
   search_fields= ['nome_editora','livros']
   list_filter = ['nome_editora','livros']


admin.site.register(Editora, MyModelAdmin)