# Generated by Django 5.0.3 on 2024-03-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('description', models.TextField()),
                ('premiere_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('production_date', models.DateField()),
                ('actor', models.ManyToManyField(to='cinema_front.actor')),
            ],
        ),
    ]
