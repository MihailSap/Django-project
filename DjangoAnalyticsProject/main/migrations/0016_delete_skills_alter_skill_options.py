# Generated by Django 5.0.4 on 2025-01-19 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_skill_alter_geography_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Skills',
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name': 'Навык', 'verbose_name_plural': 'Навык'},
        ),
    ]
