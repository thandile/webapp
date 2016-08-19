# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-19 19:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('programs', '0006_auto_20160817_1408'),
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_enrolled', models.DateField(auto_now_add=True, help_text='The date the patient was enrolled into the program.', verbose_name='date of enrollment')),
                ('comment', models.TextField(help_text='A comment on the enrollment', verbose_name='comment')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this enrollment is still active.', verbose_name='is open')),
                ('enrolled_by', models.ForeignKey(blank=True, help_text="The user that registers a patient's enrollment into a program.", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registered_enrollments', related_query_name='registered_enrollment', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(help_text='The patient enrolled in the program.', on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', related_query_name='enrollment', to='patients.Patient')),
                ('program', models.ForeignKey(help_text='The program to which a patient is enrolled', on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', related_query_name='enrollment', to='programs.Program')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='enrolled_programs',
            field=models.ManyToManyField(related_name='enrolled_patients', related_query_name='enrolled_patient', through='patients.Enrollment', to='programs.Program'),
        ),
    ]
