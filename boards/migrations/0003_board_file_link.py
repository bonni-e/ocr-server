# Generated by Django 4.2.3 on 2023-07-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='file_link',
            field=models.URLField(blank=True, editable=False, null=True),
        ),
    ]
