# Generated by Django 2.2.1 on 2019-06-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuario',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('correo', models.EmailField(max_length=30)),
                ('usuario', models.CharField(max_length=15)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
    ]
