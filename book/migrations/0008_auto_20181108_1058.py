# Generated by Django 2.1.3 on 2018-11-08 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_auto_20181108_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat_chart',
            name='train',
        ),
        migrations.DeleteModel(
            name='Seat_Chart',
        ),
    ]