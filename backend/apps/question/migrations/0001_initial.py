# Generated by Django 5.1.2 on 2024-11-10 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sesion',
            fields=[
                ('sesion_id', models.IntegerField(primary_key=True, serialize=False)),
                ('sesion_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('date_start', models.DateTimeField(null=True)),
                ('date_end', models.DateTimeField(null=True)),
            ],
        ),
    ]