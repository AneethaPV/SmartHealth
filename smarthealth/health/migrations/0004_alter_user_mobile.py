# Generated by Django 3.2.14 on 2023-03-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_healthblog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]