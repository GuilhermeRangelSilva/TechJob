# Generated by Django 5.1.1 on 2024-09-29 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='cnpj',
            field=models.CharField(max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='CNPJ deve ter 14 dígitos e conter apenas números.', regex='^\\d{14}$')]),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='CPF deve ter 11 dígitos e conter apenas números.', regex='^\\d{11}$')]),
        ),
    ]
