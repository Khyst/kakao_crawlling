# Generated by Django 2.2.1 on 2019-11-30 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20191201_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='totalamount',
            name='num',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img_id',
            field=models.IntegerField(default='1'),
        ),
        migrations.AlterField(
            model_name='totalamount',
            name='total_amount',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='totalamount',
            name='total_step',
            field=models.IntegerField(default='0'),
        ),
    ]
