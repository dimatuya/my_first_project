# Generated by Django 2.2.8 on 2019-12-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Город'),
        ),
    ]