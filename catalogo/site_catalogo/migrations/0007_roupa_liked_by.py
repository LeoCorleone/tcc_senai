# Generated by Django 4.2.5 on 2023-11-04 17:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_catalogo', '0006_remove_modelo_descricao_modelo'),
    ]

    operations = [
        migrations.AddField(
            model_name='roupa',
            name='liked_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
