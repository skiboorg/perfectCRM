# Generated by Django 3.1.6 on 2021-03-08 10:16

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20210308_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='footer_company',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Название организации'),
        ),
    ]
