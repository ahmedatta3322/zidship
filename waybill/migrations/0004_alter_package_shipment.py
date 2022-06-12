# Generated by Django 4.0.5 on 2022-06-12 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('waybill', '0003_alter_waybill_carrier_alter_waybill_receiver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='shipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='packages', to='waybill.shipment'),
        ),
    ]