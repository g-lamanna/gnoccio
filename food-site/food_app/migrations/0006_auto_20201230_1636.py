# Generated by Django 3.1.4 on 2020-12-30 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_auto_20201230_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='dessert_post',
            name='event',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='dinner_post',
            name='event',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='snack_post',
            name='event',
            field=models.IntegerField(default=1),
        ),
    ]
