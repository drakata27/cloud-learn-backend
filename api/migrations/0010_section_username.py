# Generated by Django 4.2.5 on 2024-07-20 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_section_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='username',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]