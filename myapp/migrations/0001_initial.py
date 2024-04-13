# Generated by Django 5.0.4 on 2024-04-12 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstCat',
            fields=[
                ('m1Fld1', models.AutoField(primary_key=True, serialize=False)),
                ('m1Fld2', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SecondCat',
            fields=[
                ('m2Fld1', models.AutoField(primary_key=True, serialize=False)),
                ('m2Fld3', models.CharField(max_length=100)),
                ('m2Fld2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.firstcat')),
            ],
        ),
        migrations.CreateModel(
            name='Adds',
            fields=[
                ('m3Fld1', models.AutoField(primary_key=True, serialize=False)),
                ('m3Fld3', models.CharField(max_length=100)),
                ('m3Fld2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.secondcat')),
            ],
        ),
    ]
