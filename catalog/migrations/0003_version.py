# Generated by Django 4.2.5 on 2023-09-30 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_contact_alter_product_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=2, max_digits=4)),
                ('name', models.CharField(max_length=200)),
                ('current_version_indicator', models.BooleanField(default=True)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product')),
            ],
        ),
    ]