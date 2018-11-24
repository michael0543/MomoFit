# Generated by Django 2.1.3 on 2018-11-23 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('momofit', '0003_auto_20181124_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('food_id', models.AutoField(db_column='food_id', primary_key=True, serialize=False)),
                ('food', models.CharField(db_column='food', max_length=50)),
                ('kcal', models.FloatField(db_column='kcal')),
            ],
        ),
        migrations.CreateModel(
            name='FoodRecord',
            fields=[
                ('fr_id', models.AutoField(db_column='fr_id', primary_key=True, serialize=False)),
                ('quantity', models.FloatField(db_column='quantity')),
                ('food_id', models.ForeignKey(db_column='food_id', on_delete=django.db.models.deletion.DO_NOTHING, to='momofit.FoodItem')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(db_column='store_id', primary_key=True, serialize=False)),
                ('store_name', models.CharField(db_column='store_name', max_length=50)),
                ('address', models.CharField(db_column='address', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='gymlist',
            name='name',
            field=models.CharField(db_column='name', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default='Male', max_length=6),
        ),
        migrations.AddField(
            model_name='foodrecord',
            name='user',
            field=models.ForeignKey(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='fooditem',
            name='store',
            field=models.ForeignKey(db_column='store_id', on_delete=django.db.models.deletion.DO_NOTHING, to='momofit.Store'),
        ),
    ]
