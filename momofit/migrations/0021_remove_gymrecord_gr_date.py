# Generated by Django 2.1.3 on 2018-12-07 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('momofit', '0020_auto_20181206_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymrecord',
            name='gr_date',
        ),
    ]
