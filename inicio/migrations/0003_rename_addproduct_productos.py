# Generated by Django 4.2.5 on 2023-10-03 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_rename_agregar_producto_addproduct'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AddProduct',
            new_name='Productos',
        ),
    ]
