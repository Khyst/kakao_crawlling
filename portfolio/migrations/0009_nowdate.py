# Generated by Django 2.2.1 on 2019-12-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20191201_1718'),
    ]

    operations = [
        migrations.CreateModel(
            name='nowDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nowDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
