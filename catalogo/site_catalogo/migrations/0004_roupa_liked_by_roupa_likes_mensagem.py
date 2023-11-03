# Generated by Django 4.2.3 on 2023-11-01 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_catalogo', '0003_alter_roupa_imagem_roupa'),
    ]

    operations = [
        migrations.AddField(
            model_name='roupa',
            name='liked_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='roupa',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.TextField()),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('remetente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('roupa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_catalogo.roupa')),
            ],
        ),
    ]