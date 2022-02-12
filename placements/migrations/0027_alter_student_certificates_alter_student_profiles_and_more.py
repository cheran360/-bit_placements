# Generated by Django 4.0.dev20210401123330 on 2021-12-18 15:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0026_alter_student_certificates_alter_student_profiles_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='certificates',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=1000), default=list, size=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='profiles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=1000), default=list, size=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='projectslinks',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.URLField(max_length=1000), default=list, size=20),
        ),
    ]
