# Generated by Django 4.1.3 on 2022-11-23 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0002_bank_bill_billdetail_measureunit_paymentmethod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Costo total'),
        ),
    ]