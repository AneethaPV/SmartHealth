# Generated by Django 3.2.14 on 2023-04-17 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0009_reviewrating'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='nid',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='health.nutritionist'),
            preserve_default=False,
        ),
    ]