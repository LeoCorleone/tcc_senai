# Generated by Django 4.2.3 on 2023-12-07 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_catalogo', '0002_faleconosco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faleconosco',
            old_name='texto',
            new_name='mensagem',
        ),
        migrations.AlterField(
            model_name='faleconosco',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]