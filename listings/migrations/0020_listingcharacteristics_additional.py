# Generated by Django 4.1.1 on 2023-02-06 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0019_alter_listingcharacteristics_balcony'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingcharacteristics',
            name='additional',
            field=models.CharField(default=None, max_length=50),
        ),
    ]