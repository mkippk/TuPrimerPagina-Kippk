# Generated by Django 4.2.5 on 2023-10-03 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0004_productos_descripción'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='Descripción',
            new_name='Descripcion',
        ),
    ]
