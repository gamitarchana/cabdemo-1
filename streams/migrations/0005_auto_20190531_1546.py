# Generated by Django 2.1.8 on 2019-05-31 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streams', '0004_placedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placedetail',
            name='map_icon',
            field=models.ImageField(upload_to='icons/'),
        ),
    ]
