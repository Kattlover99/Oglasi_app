# Generated by Django 4.1.1 on 2023-03-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_identification_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.FileField(max_length=255, null=True, upload_to='users'),
        ),
    ]
