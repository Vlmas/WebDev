# Generated by Django 2.1.5 on 2021-04-06 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210407_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='productitem',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]