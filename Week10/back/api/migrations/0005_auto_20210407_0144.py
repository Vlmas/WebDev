# Generated by Django 2.1.5 on 2021-04-06 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210407_0129'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productitem',
            name='count',
        ),
        migrations.RemoveField(
            model_name='productitem',
            name='is_active',
        ),
    ]
