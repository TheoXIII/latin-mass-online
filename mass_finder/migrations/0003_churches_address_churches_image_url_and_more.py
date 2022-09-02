# Generated by Django 4.1 on 2022-08-22 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mass_finder', '0002_remove_churches_mass_types_churches_high_mass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='churches',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='churches',
            name='image_url',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='churches',
            name='mass_times',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='churches',
            name='website',
            field=models.CharField(default='', max_length=255),
        ),
    ]