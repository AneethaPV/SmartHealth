# Generated by Django 3.2.14 on 2023-03-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0004_alter_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthdetails',
            name='medcond',
            field=models.CharField(max_length=200),
        ),
    ]
