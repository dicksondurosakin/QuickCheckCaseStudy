# Generated by Django 4.1.3 on 2022-12-04 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CaseStudy2', '0005_remove_news_descendants_remove_news_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='kids',
        ),
    ]
