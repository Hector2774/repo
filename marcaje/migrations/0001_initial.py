# Generated by Django 5.2 on 2025-05-13 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_externo', models.IntegerField(unique=True)),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('es_encargado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPermisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionEmpleadoEncargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_asignacion', models.DateField(auto_now_add=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encargado_asignado', to='marcaje.empleado', unique=True)),
                ('encargado', models.ForeignKey(limit_choices_to={'es_encargado': True}, on_delete=django.db.models.deletion.CASCADE, related_name='empleados_asignados', to='marcaje.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Marcaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField(verbose_name='Fecha y hora de registro')),
                ('tipo_registro', models.CharField(choices=[('I', 'Entrada'), ('O', 'Salida')], max_length=1, verbose_name='Tipo de marcaje')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcaje.empleado', verbose_name='Empleado')),
            ],
        ),
        migrations.CreateModel(
            name='MarcajeDepurado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('entrada', models.TimeField(null=True)),
                ('salida', models.TimeField(null=True)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcaje.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('fecha_solicitud', models.DateTimeField(auto_now=True)),
                ('descripcion', models.CharField(max_length=300)),
                ('estado_solicitud', models.CharField(choices=[('P', 'Pendiente'), ('A', 'Aprobada'), ('R', 'Rechazada')], default='P')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcaje.empleado')),
                ('encargado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='solicitudes_enviadas', to='marcaje.empleado')),
                ('tipo_permiso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marcaje.tipopermisos')),
            ],
        ),
        migrations.CreateModel(
            name='PermisoComprobante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprobante', models.FileField(upload_to='')),
                ('Permiso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marcaje.permisos')),
            ],
        ),
        migrations.CreateModel(
            name='GestionPermisoDetalle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accion_realizada', models.CharField(max_length=100)),
                ('revisada_por', models.CharField(max_length=100)),
                ('comentarios', models.CharField(max_length=300)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marcaje.permisos')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='marcaje.sucursal'),
        ),
    ]
