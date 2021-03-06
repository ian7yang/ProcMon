# Generated by Django 3.0.6 on 2020-08-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_crawler'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='is_alexa',
            field=models.BooleanField(default=False),
        ),
    ]
