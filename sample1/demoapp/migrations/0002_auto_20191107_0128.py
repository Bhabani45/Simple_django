# Generated by Django 2.2.6 on 2019-11-07 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Customer_Email',
            new_name='Employee_Email',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Customer_ID',
            new_name='Employee_ID',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='Customer_Name',
            new_name='Employee_Name',
        ),
        migrations.AlterModelTable(
            name='customer',
            table='Employee',
        ),
    ]