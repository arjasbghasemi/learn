# Generated by Django 5.1.4 on 2024-12-12 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_lesson_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subsubcategory',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
        ),
    ]
