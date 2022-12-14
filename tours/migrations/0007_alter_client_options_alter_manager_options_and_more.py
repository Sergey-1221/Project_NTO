# Generated by Django 4.1.3 on 2022-11-23 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_client_phone'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиент', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Контактное лицо', 'verbose_name_plural': 'Контактные лица'},
        ),
        migrations.AddField(
            model_name='tours',
            name='date_of_exit',
            field=models.DateField(null=True, verbose_name='Дата выезда'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='tours',
            name='date_of_stay',
            field=models.DateField(null=True, verbose_name='Дата заезда'),
        ),
    ]
