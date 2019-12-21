# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-11 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Absen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=100)),
                ('nama_belakang', models.CharField(max_length=100)),
                ('kelas', models.CharField(choices=[('x', 'X'), ('xi', 'XI'), ('xii', 'XII')], default='x', max_length=20)),
                ('jurusan', models.CharField(choices=[('tkj', 'Teknik Komputer dan Jaringan'), ('rpl', 'Rekayasa Perangkat Lunak'), ('pbs', 'Perbankan Syariah'), ('kt', 'Kriya Tekstil'), ('tkr', 'Teknik Kendaraan Ringan')], default='tkj', max_length=100)),
                ('alamat', models.TextField()),
            ],
        ),
    ]
