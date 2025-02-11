# Generated by Django 4.2 on 2025-01-24 09:45

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
