# Generated by Django 4.2.10 on 2024-03-02 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_itenssaida_material_itenssaida_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itenssaida',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.material'),
        ),
    ]
