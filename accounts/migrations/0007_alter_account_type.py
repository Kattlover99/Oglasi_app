# Generated by Django 4.1.1 on 2023-03-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type',
            field=models.CharField(choices=[('0', 'Fizičko lice'), ('1', 'Pravno lice')], default='0', max_length=25),
        ),
    ]
