# Generated by Django 2.2.1 on 2019-11-30 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_portfolio_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='totalAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_step', models.IntegerField(default=0)),
                ('total_amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='img_id',
            field=models.IntegerField(default=1),
        ),
    ]
