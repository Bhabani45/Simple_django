# Generated by Django 2.2.7 on 2019-11-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Venue Name')),
                ('address', models.CharField(max_length=300)),
                ('zipcode', models.CharField(max_length=12, verbose_name='Zip/Post Code')),
                ('phone', models.CharField(max_length=20, verbose_name='Contact Phone')),
                ('web', models.URLField(verbose_name='Web Address')),
                ('email_address', models.EmailField(max_length=254, verbose_name='Email Address')),
            ],
        ),
    ]