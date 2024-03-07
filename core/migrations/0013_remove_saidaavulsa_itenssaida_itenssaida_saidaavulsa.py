# Generated by Django 4.2.10 on 2024-03-02 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_saidaavulsa_itenssaida'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saidaavulsa',
            name='itensSaida',
        ),
        migrations.AddField(
            model_name='itenssaida',
            name='saidaAvulsa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.saidaavulsa'),
        ),
    ]
