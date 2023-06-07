# Generated by Django 4.1.7 on 2023-04-11 06:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_id', models.CharField(max_length=6)),
                ('car_number', models.CharField(max_length=15)),
                ('rent_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='carrentals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_id', models.CharField(max_length=15)),
                ('rent_date', models.DateField()),
                ('arrive_time', models.TimeField()),
                ('date_return', models.DateField()),
                ('payment_amount', models.IntegerField()),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car.car')),
            ],
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_id', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='./userprofile/')),
                ('nid', models.CharField(max_length=15)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='cartransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_id', models.CharField(max_length=50)),
                ('tras_date', models.DateField()),
                ('carrentals', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car.carrentals')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='car.driver'),
        ),
    ]
