# Generated by Django 3.0.1 on 2020-02-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20200221_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eval',
            name='text',
            field=models.TextField(null=True),
        ),
    ]