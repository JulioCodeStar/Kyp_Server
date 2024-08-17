# Generated by Django 5.0.7 on 2024-08-17 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_paciente', models.CharField(max_length=10)),
                ('dni', models.IntegerField(max_length=20)),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=20)),
                ('otro_contact', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=255)),
                ('locacion', models.CharField(max_length=100)),
                ('edad', models.IntegerField(max_length=3)),
                ('sede', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=100)),
                ('time_ampu', models.CharField(max_length=255)),
                ('motivo', models.CharField(max_length=255)),
                ('canal', models.CharField(max_length=100)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('fecha_nac', models.DateField()),
                ('email_pat', models.EmailField(blank=True, max_length=254, null=True)),
                ('afecciones', models.CharField(blank=True, max_length=100, null=True)),
                ('alergias', models.CharField(blank=True, max_length=100, null=True)),
                ('vendedor', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'kyp_pacientes',
            },
        ),
    ]
