# Generated by Django 2.2.5 on 2019-11-06 08:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notificationprofile', '0003_delete_notificationprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('filter_string', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlotGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slot_groups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('MO', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=2)),
                ('start', models.TimeField(help_text='Local time.')),
                ('end', models.TimeField(help_text='Local time.')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slots', to='notificationprofile.TimeSlotGroup')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationProfile',
            fields=[
                ('media', multiselectfield.db.fields.MultiSelectField(choices=[('EM', 'Email'), ('SM', 'SMS'), ('SL', 'Slack')], default='EM', max_length=8)),
                ('active', models.BooleanField(default=True)),
                ('filters', models.ManyToManyField(related_name='notification_profiles', to='notificationprofile.Filter')),
                ('time_slot_group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='notification_profile', serialize=False, to='notificationprofile.TimeSlotGroup')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='filter',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_name_per_user'),
        ),
        migrations.AddConstraint(
            model_name='timeslotgroup',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='unique_name_per_user'),
        ),
    ]