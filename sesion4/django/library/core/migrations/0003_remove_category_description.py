# Generated by Django 3.2.6 on 2021-08-07 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
    ]