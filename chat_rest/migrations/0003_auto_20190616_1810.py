# Generated by Django 2.2.2 on 2019-06-16 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_rest', '0002_auto_20190616_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
