# Generated by Django 5.1.4 on 2024-12-07 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printers', '0002_snmpoid_snmphistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='community',
            field=models.CharField(default='public', max_length=255),
        ),
    ]