# Generated by Django 4.2.5 on 2024-09-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_section_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
