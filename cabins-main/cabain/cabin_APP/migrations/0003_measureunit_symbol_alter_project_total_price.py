# Generated by Django 4.0.4 on 2022-11-25 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0002_bank_bill_billdetail_measureunit_paymentmethod_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='measureunit',
            name='symbol',
            field=models.CharField(default=int, max_length=20, verbose_name='Símbolo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='total_price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Costo total'),
        ),
    ]
