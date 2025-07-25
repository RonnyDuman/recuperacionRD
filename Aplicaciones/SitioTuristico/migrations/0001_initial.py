# Generated by Django 5.2.1 on 2025-07-25 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SitioTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('requiere_visa', models.BooleanField(default=False)),
                ('foto_principal', models.FileField(upload_to='sitios/fotos_principales/')),
                ('foto_secundaria', models.FileField(upload_to='sitios/fotos_secundarias/')),
                ('historia_pdf', models.FileField(upload_to='sitios/historias/')),
                ('fecha_fundacion', models.DateField()),
                ('email_contacto', models.EmailField(max_length=254)),
                ('telefono_contacto', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=128)),
            ],
        ),
    ]
