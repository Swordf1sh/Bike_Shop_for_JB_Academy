# Generated by Django 4.1.1 on 2024-01-01 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('description', models.TextField()),
                ('has_basket', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=56)),
                ('quantity', models.IntegerField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bike')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('surname', models.CharField(max_length=56)),
                ('phone_number', models.CharField(max_length=56)),
                ('status', models.CharField(choices=[('P', 'pending'), ('R', 'ready')], max_length=10)),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bike')),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=56)),
                ('quantity', models.IntegerField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bike')),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.bike')),
            ],
        ),
    ]