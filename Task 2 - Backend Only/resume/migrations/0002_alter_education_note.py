# Generated by Django 3.2.6 on 2021-08-18 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
