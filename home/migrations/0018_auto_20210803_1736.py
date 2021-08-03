# Generated by Django 3.2.4 on 2021-08-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_buytoken_token_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buytoken',
            name='gbp_amount',
            field=models.DecimalField(decimal_places=30, default=0, max_digits=30),
        ),
        migrations.AlterField(
            model_name='buytoken',
            name='token_amount',
            field=models.DecimalField(decimal_places=30, default=0, max_digits=30),
        ),
        migrations.AlterField(
            model_name='buytoken',
            name='token_price',
            field=models.DecimalField(decimal_places=30, default=0, max_digits=30),
        ),
    ]
