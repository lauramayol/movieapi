# Generated by Django 2.1.2 on 2018-10-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_link', models.CharField(max_length=100)),
                ('movie_name', models.CharField(max_length=150)),
                ('narrative_location', models.CharField(max_length=100)),
                ('coordinates', models.CharField(max_length=100)),
            ],
        ),
    ]
