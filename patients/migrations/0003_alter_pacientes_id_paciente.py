# Generated by Django 5.0.7 on 2024-08-28 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_alter_pacientes_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacientes',
            name='id_paciente',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
