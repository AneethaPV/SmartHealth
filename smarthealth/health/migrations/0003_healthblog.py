# Generated by Django 3.2.14 on 2023-02-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0002_remove_notification_lid'),
    ]

    operations = [
        migrations.CreateModel(
            name='healthblog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.CharField(max_length=50)),
                ('date', models.DateField()),
            ],
        ),
    ]
