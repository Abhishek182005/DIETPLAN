# Generated by Django 5.1.7 on 2025-03-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, help_text='Upload an image of the prepared dish', null=True, upload_to='recipes/'),
        ),
    ]
