# Generated by Django 4.1 on 2022-09-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_publishers_alter_comics_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comics',
            name='time_purchase',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
