# Generated by Django 5.1.4 on 2024-12-20 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='media/'),
        ),
    ]
