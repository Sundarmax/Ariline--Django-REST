# Generated by Django 2.1.1 on 2018-09-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0002_auto_20180921_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='flight_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_dep_date', models.DateField()),
                ('price', models.IntegerField()),
                ('avail_seats', models.IntegerField()),
            ],
        ),
    ]
