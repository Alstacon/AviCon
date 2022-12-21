# Generated by Django 4.1.4 on 2022-12-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(choices=[('user', 'Пользователь'), ('admin', 'Администратор')], default='user', max_length=5)),
                ('image', models.ImageField(default=None, null=True, upload_to='avatars/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]