# Generated by Django 2.1.7 on 2019-03-06 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prefMovie', '0007_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='comment',
        ),
    ]
