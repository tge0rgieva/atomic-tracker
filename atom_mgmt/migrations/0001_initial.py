# Generated by Django 3.0.8 on 2020-07-19 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atom_status', models.CharField(max_length=12)),
                ('atom_name', models.CharField(max_length=16)),
                ('atom_desc', models.CharField(max_length=256)),
                ('atom_category', models.CharField(max_length=24)),
                ('track_frequency', models.CharField(max_length=24)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='user_mgmt.Users')),
            ],
        ),
    ]