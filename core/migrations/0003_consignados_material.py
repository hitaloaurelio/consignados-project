# Generated by Django 4.2.10 on 2024-03-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_consignados'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignados',
            name='material',
            field=models.ManyToManyField(blank=True, null=True, to='core.material'),
        ),
    ]