# Generated by Django 4.2.17 on 2025-02-06 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_lesson_main_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='value',
        ),
    ]
