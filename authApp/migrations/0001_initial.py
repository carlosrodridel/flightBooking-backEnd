# Generated by Django 3.2.8 on 2021-10-18 23:36

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, null=True, verbose_name='EmailUser')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cedula', models.IntegerField()),
                ('nombre', models.CharField(max_length=50, verbose_name='Name')),
                ('celular', models.BigIntegerField()),
                ('correo', models.EmailField(max_length=100, verbose_name='Email')),
                ('userP', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CreadorPasajero', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('sillas', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None)),
                ('ciudad_origen', models.CharField(max_length=50, verbose_name='Origen')),
                ('ciudad_destino', models.CharField(max_length=50, verbose_name='Destino')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CreadorVuelo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tiquete',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.pasajero')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vuelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authApp.vuelo')),
            ],
        ),
    ]
