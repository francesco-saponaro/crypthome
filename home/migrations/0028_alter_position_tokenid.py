# Generated by Django 3.2.4 on 2021-08-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0027_auto_20210811_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='tokenid',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]