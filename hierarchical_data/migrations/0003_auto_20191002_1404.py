# Generated by Django 2.2.6 on 2019-10-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hierarchical_data', '0002_auto_20191002_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_class',
            name='file_link',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
