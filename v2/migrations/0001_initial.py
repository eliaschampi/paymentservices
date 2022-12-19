# Generated by Django 4.1.4 on 2022-12-19 04:10

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
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('payment_date', models.DateTimeField()),
                ('expiration_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ser_users', to='v2.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pay_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpiredPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalti_fee_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('payment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expired_pay_users', to='v2.paymentuser')),
            ],
        ),
    ]
