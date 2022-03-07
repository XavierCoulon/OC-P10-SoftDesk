# Generated by Django 4.0.2 on 2022-03-07 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_unique_together'),
        ('users', '0006_remove_customuser_is_admin'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='contributor',
            unique_together={('user_id', 'project_id')},
        ),
    ]
