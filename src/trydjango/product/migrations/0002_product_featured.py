# Generated by Django 2.1.5 on 2020-09-22 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Featured',
            field=models.BooleanField(default=True),
        ),
    ]
