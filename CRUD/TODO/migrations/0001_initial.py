# Generated by Django 4.2.9 on 2024-01-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
