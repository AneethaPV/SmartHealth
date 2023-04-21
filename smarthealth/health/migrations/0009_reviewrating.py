# Generated by Django 3.2.14 on 2023-04-11 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0008_remove_healthdetails_gweight'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewrating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=60)),
                ('rating', models.FloatField()),
                ('date', models.DateField()),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.user')),
            ],
        ),
    ]