# Generated by Django 3.1.7 on 2021-11-25 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211125_0031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='category_Animal',
            new_name='RAÇA_Animal',
        ),
        migrations.RenameField(
            model_name='banhoetosa',
            old_name='category',
            new_name='serviços',
        ),
    ]