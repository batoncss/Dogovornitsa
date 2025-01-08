# Generated by Django 5.1.4 on 2025-01-04 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_participant_actual_address_participant_kpp_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование шаблона')),
                ('body', models.TextField(verbose_name='Тело шаблона')),
            ],
        ),
        migrations.AlterField(
            model_name='participant',
            name='inn',
            field=models.CharField(default='', max_length=12, null=True, unique=True, verbose_name='ИНН'),
        ),
    ]
