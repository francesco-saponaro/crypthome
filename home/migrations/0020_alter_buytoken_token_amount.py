# Generated by Django 3.2.4 on 2021-08-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210803_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buytoken',
            name='token_amount',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=30),
        ),
    ]