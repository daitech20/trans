# Generated by Django 3.2.7 on 2022-05-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='from_country',
            field=models.CharField(choices=[('US', 'USA'), ('VN', 'Viet Nam')], max_length=20),
        ),
        migrations.AlterField(
            model_name='information',
            name='to_country',
            field=models.CharField(choices=[('US', 'USA'), ('VN', 'Viet Nam')], max_length=20),
        ),
    ]
