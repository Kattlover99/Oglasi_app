# Generated by Django 4.1.1 on 2023-02-03 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='slug',
            field=models.SlugField(default='', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='listingcharacteristics',
            name='floor',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='listingcharacteristics',
            name='total_floors',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='listingcharacteristics',
            name='year_built',
            field=models.IntegerField(default=None, null=True),
        ),
    ]