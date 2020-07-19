# Generated by Django 3.0.8 on 2020-07-19 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atom_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atom_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='atom_mgmt.Atom')),
            ],
        ),
    ]