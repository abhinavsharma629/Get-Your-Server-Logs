# Generated by Django 2.1.5 on 2019-02-02 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webap', '0003_auto_20190202_1147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id_no',
        ),
    ]