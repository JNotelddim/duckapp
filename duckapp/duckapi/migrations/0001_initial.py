# Generated by Django 2.0.3 on 2019-10-25 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedingSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feeding_time', models.DateTimeField()),
                ('food', models.CharField(max_length=100)),
                ('food_type', models.CharField(max_length=100)),
                ('food_quantity', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('duck_count', models.IntegerField()),
            ],
        ),
    ]
