# Generated by Django 5.0.6 on 2024-07-19 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reporte_mensual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion_mensual', models.DateField(auto_now_add=True)),
                ('produccion_total_mensual', models.IntegerField()),
                ('produccion_defectuosa_mensual', models.FloatField()),
                ('tasa_defectuosa_mensual', models.BigIntegerField()),
                ('tiempo_operacion_mensual', models.BigIntegerField()),
                ('tiempo_inactividad_mensual', models.BigIntegerField()),
                ('calidad_mensual', models.FloatField()),
                ('oee_mensual', models.FloatField()),
                ('maquina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitoreo.maquinaproductiva', verbose_name='reporte_maquina_mensual')),
            ],
        ),
    ]
