# Generated by Django 3.2.13 on 2023-01-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal_dev', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='dateReg',
            field=models.DateField(blank=True, null=True, verbose_name='Дата регисрации'),
        ),
    ]
