# Generated by Django 2.2.1 on 2019-11-30 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_img_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='name',
            field=models.CharField(default='201201', max_length=255),
        ),
    ]
