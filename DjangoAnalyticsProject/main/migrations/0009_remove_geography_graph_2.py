# Generated by Django 5.0.4 on 2025-01-14 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_geography_graph_2_relevance_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='geography',
            name='graph_2',
        ),
    ]
