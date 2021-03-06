# Generated by Django 2.2.9 on 2022-02-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('livro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_autor', models.CharField(max_length=255, verbose_name='nome_autor')),
                ('livro', models.ManyToManyField(related_name='Livro', to='livro.Livro')),
            ],
            options={
                'db_table': 'autor',
            },
        ),
    ]
