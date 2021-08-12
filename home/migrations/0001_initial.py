# Generated by Django 3.2.4 on 2021-08-11 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tokenid', models.CharField(blank=True, max_length=100, null=True)),
                ('symbol', models.CharField(max_length=10)),
                ('image', models.URLField()),
                ('price', models.FloatField(blank=True, default=0)),
                ('rank', models.CharField(max_length=10)),
                ('market_cap', models.CharField(max_length=200)),
                ('price_change', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='BuyToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('token_id', models.CharField(default=0, max_length=20)),
                ('token_symbol', models.CharField(max_length=10)),
                ('token_price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('gbp_amount', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('token_amount', models.DecimalField(decimal_places=4, default=0, max_digits=30)),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='token_bought', to='profiles.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_allowance', models.DecimalField(decimal_places=2, default=10000, max_digits=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='default_allowance', to='profiles.userprofile')),
            ],
        ),
    ]
