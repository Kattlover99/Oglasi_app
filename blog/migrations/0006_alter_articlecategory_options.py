# Generated by Django 4.1.1 on 2023-03-03 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_articlecategory_alter_article_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articlecategory',
            options={'verbose_name_plural': 'Article Categories'},
        ),
    ]
