# Generated by Django 2.1.5 on 2019-02-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20190202_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='current',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='goal',
            field=models.IntegerField(default=0),
        ),
    ]
