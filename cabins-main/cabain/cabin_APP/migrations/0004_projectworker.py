# Generated by Django 4.0.4 on 2022-11-30 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0003_measureunit_symbol_alter_project_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=60, verbose_name='Trabajo')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.project', verbose_name='Proyecto')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.worker', verbose_name='Trabajador')),
            ],
        ),
    ]
