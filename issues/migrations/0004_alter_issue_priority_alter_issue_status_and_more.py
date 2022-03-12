# Generated by Django 4.0.2 on 2022-03-11 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_alter_issue_assignee_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Middle', 'Middle'), ('High', 'High')], max_length=64),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('T', 'TO DO'), ('I', 'IN PROGRESS'), ('C', 'CLOSED')], max_length=64),
        ),
        migrations.AlterField(
            model_name='issue',
            name='tag',
            field=models.CharField(choices=[('B', 'BUG'), ('E', 'ENHANCEMENT'), ('T', 'TASK')], max_length=64),
        ),
    ]
