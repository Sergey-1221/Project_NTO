# Generated by Django 4.1.3 on 2022-11-29 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_remove_tours_numbers_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='price',
            field=models.FloatField(verbose_name='Стоимость тура (Руб)'),
        ),
        migrations.CreateModel(
            name='Tour_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(choices=[('Предоплата', 'Предоплата'), ('Кредит', 'Кредит')], max_length=100, verbose_name='Вид оплаты')),
                ('price', models.FloatField(default=123, verbose_name='Стоимость тура (Руб)')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.tours', verbose_name='Тур')),
                ('сlient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.client', verbose_name='Клиент')),
            ],
            options={
                'verbose_name': 'Заказ тура',
                'verbose_name_plural': 'Заказ тура',
            },
        ),
    ]
