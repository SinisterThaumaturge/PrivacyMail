# Generated by Django 2.1.7 on 2019-03-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailfetcher', '0002_thirdparty_resultsdirty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eresource',
            name='mail_leakage',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
