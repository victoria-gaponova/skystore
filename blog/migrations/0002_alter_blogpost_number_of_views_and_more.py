# Generated by Django 4.2.5 on 2023-09-24 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='number_of_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='publication_sign',
            field=models.BooleanField(default=True),
        ),
    ]
