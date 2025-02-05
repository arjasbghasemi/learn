# Generated by Django 4.2.17 on 2025-02-06 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_delete_userlessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='link_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='lesson',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='lessons/pdf/'),
        ),
    ]
