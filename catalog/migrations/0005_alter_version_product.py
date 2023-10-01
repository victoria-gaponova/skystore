# Generated by Django 4.2.5 on 2023-09-30 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_version_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product'),
        ),
    ]
