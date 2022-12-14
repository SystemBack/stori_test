# Generated by Django 4.1 on 2022-08-29 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('transactions_amount', models.IntegerField(default=None)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=100)),
                ('transaction_date', models.CharField(max_length=100)),
                ('transaction', models.CharField(max_length=100)),
                ('is_credit_card', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.update')),
            ],
        ),
    ]
