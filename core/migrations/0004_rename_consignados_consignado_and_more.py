# Generated by Django 4.2.10 on 2024-03-02 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_consignados_material'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Consignados',
            new_name='Consignado',
        ),
        migrations.AlterModelOptions(
            name='consignado',
            options={'verbose_name_plural': 'Consignações'},
        ),
        migrations.AlterModelOptions(
            name='hospital',
            options={'verbose_name_plural': 'Hospitais'},
        ),
    ]
