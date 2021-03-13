# Generated by Django 3.1.6 on 2021-03-09 05:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0020_headerservice_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blockIcon', models.FileField(null=True, upload_to='icons/', verbose_name='Иконка блока ')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='Заголовок блока')),
                ('subtitle', models.CharField(max_length=255, null=True, verbose_name='Подзаголовок блока')),
                ('block1_title', models.CharField(max_length=255, null=True, verbose_name='Заголовок блока1')),
                ('block1_subtitle', models.CharField(max_length=255, null=True, verbose_name='Подзаголовок блока1')),
                ('block1_check', models.BooleanField(blank=True, verbose_name='Показывать чекбокс в блоке1')),
                ('block1_costSubFix', models.CharField(max_length=255, null=True, verbose_name='costSubFix')),
                ('block1_costSubUser', models.CharField(max_length=255, null=True, verbose_name='costSubUser')),
                ('block1_costSubPCC', models.CharField(max_length=255, null=True, verbose_name='costSubPCC')),
                ('block2_title', models.CharField(max_length=255, null=True, verbose_name='Заголовок блока2')),
                ('block2_subtitle', models.CharField(max_length=255, null=True, verbose_name='Подзаголовок блока2')),
                ('block2_check', models.BooleanField(blank=True, verbose_name='Показывать чекбокс в блоке2')),
                ('block2_costEntFix', models.CharField(max_length=255, null=True, verbose_name='costEntFix')),
                ('block2_costEntUser', models.CharField(max_length=255, null=True, verbose_name='costEntUser')),
                ('block2_costEntPCC', models.CharField(max_length=255, null=True, verbose_name='costEntPCC')),
                ('block3_title', models.CharField(max_length=255, null=True, verbose_name='Заголовок блока3')),
                ('block3_subtitle', models.CharField(max_length=255, null=True, verbose_name='Подзаголовок блока3')),
                ('block3_info', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='Инфо в блоке')),
            ],
            options={
                'verbose_name': '7. Стоимость',
                'verbose_name_plural': '7. Стоимость',
            },
        ),
        migrations.AlterModelOptions(
            name='headerservice',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]
