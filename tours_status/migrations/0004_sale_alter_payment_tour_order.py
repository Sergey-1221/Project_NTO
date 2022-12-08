# Generated by Django 4.1.3 on 2022-12-08 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0019_alter_tour_order_status'),
        ('tours_status', '0003_remove_payment_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('tour_order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='tours_status.payment', verbose_name='Заказ')),
                ('booking', models.CharField(choices=[('Да', 'Да'), ('Нет', 'Нет')], max_length=100, verbose_name='Бронь номеров')),
            ],
            options={
                'verbose_name': 'Продажа тура',
                'verbose_name_plural': 'Продажи туров',
            },
        ),
        migrations.AlterField(
            model_name='payment',
            name='tour_order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='+', serialize=False, to='tours.tour_order', verbose_name='Заказ'),
        ),
    ]