# Generated by Django 4.2.5 on 2023-11-04 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_catalogo', '0005_remove_roupa_liked_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelo',
            name='descricao_modelo',
        ),
    ]