# Generated by Django 2.2.9 on 2022-02-17 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autor',
            old_name='livro',
            new_name='livros',
        ),
    ]