# Generated by Django 2.2.13 on 2020-11-25 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailfetcher', '0011_thirdparty_add_connections_to_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='h_subject',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
