# Generated by Django 3.2 on 2022-04-19 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_category_issubcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='isSubCategory',
            new_name='isMainCategory',
        ),
    ]
