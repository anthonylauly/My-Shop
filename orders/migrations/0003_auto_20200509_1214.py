# Generated by Django 2.2.12 on 2020-05-09 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_braintree_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'order'},
        ),
    ]
