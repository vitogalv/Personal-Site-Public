# Generated by Django 2.1.3 on 2018-11-12 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_auto_20181111_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.URLField(default='www.linkedin.com/in/vito-galvez-50413714a'),
        ),
    ]