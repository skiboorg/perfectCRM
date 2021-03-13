# Generated by Django 3.1.6 on 2021-03-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_feedback_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='footer_copyright',
            field=models.CharField(max_length=255, null=True, verbose_name='Текст копирайт'),
        ),
        migrations.AddField(
            model_name='settings',
            name='footer_link1_link',
            field=models.CharField(max_length=255, null=True, verbose_name='URL ссылки'),
        ),
        migrations.AddField(
            model_name='settings',
            name='footer_link1_text',
            field=models.CharField(max_length=255, null=True, verbose_name='Текст ссылки'),
        ),
        migrations.AddField(
            model_name='settings',
            name='footer_link2_link',
            field=models.CharField(max_length=255, null=True, verbose_name='URL ссылки'),
        ),
        migrations.AddField(
            model_name='settings',
            name='footer_link2_text',
            field=models.CharField(max_length=255, null=True, verbose_name='Текст ссылки'),
        ),
    ]
