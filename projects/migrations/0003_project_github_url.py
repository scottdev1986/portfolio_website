# Generated by Django 4.0 on 2022-01-11 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='github_url',
            field=models.URLField(default='www.google.com'),
            preserve_default=False,
        ),
    ]
