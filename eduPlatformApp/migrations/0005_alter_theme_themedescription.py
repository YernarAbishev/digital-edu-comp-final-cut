# Generated by Django 4.1.3 on 2023-04-03 16:46

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatformApp', '0004_remove_comment_name_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='themeDescription',
            field=tinymce.models.HTMLField(verbose_name='Theme Description'),
        ),
    ]
