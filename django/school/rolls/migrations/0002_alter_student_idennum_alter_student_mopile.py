# Generated by Django 4.0.4 on 2022-05-23 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rolls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='idenNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='mopile',
            field=models.CharField(default=0, max_length=11),
        ),
    ]