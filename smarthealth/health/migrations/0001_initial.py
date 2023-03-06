# Generated by Django 3.2.14 on 2023-02-23 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='foodcalories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(max_length=30)),
                ('calories', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('usertype', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='nutritionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('qualification', models.CharField(max_length=20)),
                ('experience', models.IntegerField()),
                ('license', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('mobile', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.login')),
            ],
        ),
        migrations.CreateModel(
            name='reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine', models.CharField(max_length=30)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('dose', models.TimeField()),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.login')),
            ],
        ),
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.login')),
            ],
        ),
        migrations.CreateModel(
            name='healthdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('height', models.FloatField()),
                ('cweight', models.FloatField()),
                ('gweight', models.FloatField()),
                ('medcond', models.FloatField()),
                ('bmi', models.FloatField()),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.login')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('reply', models.CharField(max_length=30)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.user')),
            ],
        ),
        migrations.CreateModel(
            name='calories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('breakfast', models.IntegerField()),
                ('lunch', models.IntegerField()),
                ('dinner', models.IntegerField()),
                ('lid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='health.login')),
            ],
        ),
    ]