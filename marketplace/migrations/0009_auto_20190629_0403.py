# Generated by Django 2.1.2 on 2019-06-29 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_auto_20190629_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
