# Generated by Django 5.1.5 on 2025-01-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='journalentry',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='journalentry',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
