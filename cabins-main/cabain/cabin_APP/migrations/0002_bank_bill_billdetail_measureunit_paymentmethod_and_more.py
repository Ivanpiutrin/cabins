# Generated by Django 4.0.4 on 2022-10-31 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cabin_APP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=30, verbose_name='Banco')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.IntegerField(verbose_name='Número de factura')),
                ('emision_date', models.DateTimeField(verbose_name='Fecha de emisión')),
                ('supplier_rut', models.CharField(max_length=12, verbose_name='Rut proveedor')),
                ('supplier_names', models.CharField(max_length=60, verbose_name='Nombre proveedor')),
                ('supplier_last_names', models.CharField(blank=True, max_length=60, null=True, verbose_name='Apellidos proveedor')),
                ('supplier_address', models.CharField(max_length=60, verbose_name='Dirección proveedor')),
                ('seller_name', models.CharField(max_length=60, verbose_name='Nombre vendedor')),
                ('seller_last_name', models.CharField(max_length=60, verbose_name='Apellido vendedor')),
                ('observations', models.CharField(blank=True, max_length=120, null=True, verbose_name='Observaciones')),
                ('subtotal', models.IntegerField(verbose_name='Subtotal')),
                ('iva', models.IntegerField(verbose_name='IVA')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('limit_date', models.DateField(verbose_name='Fecha de vencimiento')),
                ('iban', models.CharField(blank=True, max_length=60, null=True, verbose_name='IBAN')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo electrónico')),
                ('phone', models.CharField(max_length=20, verbose_name='Número de contacto')),
                ('bank', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.bank', verbose_name='Banaco')),
            ],
        ),
        migrations.CreateModel(
            name='BillDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlative', models.IntegerField(verbose_name='Correlativo')),
                ('description', models.CharField(blank=True, max_length=120, null=True, verbose_name='Descripción')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('unitary_price', models.IntegerField(verbose_name='Precio unitario')),
                ('discount', models.IntegerField(verbose_name='Descuento')),
                ('total', models.IntegerField(verbose_name='Total')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.bill', verbose_name='Número factura')),
            ],
        ),
        migrations.CreateModel(
            name='MeasureUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=20, verbose_name='Unidad de medida')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_name', models.CharField(max_length=30, verbose_name='Método de pago')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=60, verbose_name='Nombre Proyecto')),
                ('surface', models.IntegerField(verbose_name='Superficie(m2)')),
                ('total_price', models.IntegerField(verbose_name='Costo total')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, verbose_name='Usuario')),
                ('password', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('names', models.CharField(max_length=60, verbose_name='Nombre')),
                ('last_names', models.CharField(max_length=60, verbose_name='Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('phone', models.CharField(max_length=20, verbose_name='Celular')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=60, verbose_name='Nombre')),
                ('last_names', models.CharField(max_length=60, verbose_name='Apellido')),
                ('payment', models.IntegerField(verbose_name='Costo')),
                ('balance', models.IntegerField(verbose_name='Deuda')),
            ],
        ),
        migrations.AlterField(
            model_name='city',
            name='city_name',
            field=models.CharField(max_length=30, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.region', verbose_name='Región'),
        ),
        migrations.AlterField(
            model_name='region',
            name='region_name',
            field=models.CharField(max_length=30, verbose_name='Región'),
        ),
        migrations.CreateModel(
            name='ProjectDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Cantidad')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.billdetail', verbose_name='Producto')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.project', verbose_name='Proyecto')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.user', verbose_name='Usuario'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=30, verbose_name='Nombre del producto')),
                ('category', models.CharField(max_length=30, verbose_name='Categoría')),
                ('measure_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.measureunit', verbose_name='Unidad de medida')),
            ],
        ),
        migrations.CreateModel(
            name='Commune',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commune_name', models.CharField(max_length=30, verbose_name='Comuna')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.city', verbose_name='Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_rut', models.CharField(max_length=12, verbose_name='Rut Cliente')),
                ('client_name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('client_last_name', models.CharField(max_length=60, verbose_name='Apellido')),
                ('client_address', models.CharField(max_length=60, verbose_name='Dirección cliente')),
                ('client_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.city', verbose_name='Ciudad cliente')),
                ('client_commune', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.commune', verbose_name='Comuna cliente')),
            ],
        ),
        migrations.AddField(
            model_name='billdetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.product', verbose_name='Producto'),
        ),
        migrations.AddField(
            model_name='bill',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.client', verbose_name='Cliente'),
        ),
        migrations.AddField(
            model_name='bill',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.paymentmethod', verbose_name='Método de pago'),
        ),
        migrations.AddField(
            model_name='bill',
            name='supplier_city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.city', verbose_name='Ciudad proveedor'),
        ),
        migrations.AddField(
            model_name='bill',
            name='supplier_commune',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cabin_APP.commune', verbose_name='Comuna'),
        ),
    ]
