# Generated by Django 4.0.dev20210401123330 on 2021-12-10 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0007_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='placements.company'),
        ),
    ]
