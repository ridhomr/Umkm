# Generated by Django 3.0.5 on 2020-06-15 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_order_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='address',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
