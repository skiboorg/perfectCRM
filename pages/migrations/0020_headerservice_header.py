# Generated by Django 3.1.6 on 2021-03-09 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_headerservice'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerservice',
            name='header',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='pages.header'),
        ),
    ]
