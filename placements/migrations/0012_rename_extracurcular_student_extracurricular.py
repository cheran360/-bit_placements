# Generated by Django 4.0.dev20210401123330 on 2021-12-10 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placements', '0011_student_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='extracurcular',
            new_name='extracurricular',
        ),
    ]