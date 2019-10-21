# Generated by Django 2.2.5 on 2019-10-15 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkSystemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ParentObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('parentobject_id', models.CharField(blank=True, max_length=20, verbose_name='parent object ID')),
                ('url', models.URLField(verbose_name='URL')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProblemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('object_id', models.CharField(blank=True, max_length=20, verbose_name='object ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('network_system', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objects', to='alert.NetworkSystem')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='alert.ObjectType')),
            ],
        ),
        migrations.AddField(
            model_name='networksystem',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instances', to='alert.NetworkSystemType'),
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('alert_id', models.CharField(max_length=20, verbose_name='alert ID')),
                ('details_url', models.URLField(blank=True, verbose_name='details URL')),
                ('description', models.TextField(blank=True)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='alert.Object')),
                ('parent_object', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='alert.ParentObject')),
                ('problem_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='alert.ProblemType')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alerts', to='alert.NetworkSystem', verbose_name='network system source')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.AddConstraint(
            model_name='object',
            constraint=models.UniqueConstraint(fields=('object_id', 'network_system'), name='unique_object_id_per_network_system'),
        ),
        migrations.AddConstraint(
            model_name='object',
            constraint=models.UniqueConstraint(fields=('name', 'type', 'network_system'), name='unique_name_and_type_per_network_system'),
        ),
        migrations.AddConstraint(
            model_name='alert',
            constraint=models.UniqueConstraint(fields=('alert_id', 'source'), name='unique_alert_id_per_source'),
        ),
    ]