# Generated by Django 2.1.7 on 2019-03-06 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prefMovie', '0005_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
