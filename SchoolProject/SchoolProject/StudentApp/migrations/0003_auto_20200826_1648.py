# Generated by Django 3.1 on 2020-08-26 11:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('StudentApp', '0002_auto_20200806_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
