# Generated by Django 5.0.6 on 2024-07-29 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0003_usuario_is_active_usuario_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
