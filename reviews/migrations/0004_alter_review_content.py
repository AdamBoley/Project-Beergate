# Generated by Django 3.2.15 on 2022-09-08 16:42

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_alter_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
