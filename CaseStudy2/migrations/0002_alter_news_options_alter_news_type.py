# Generated by Django 4.1.3 on 2022-12-03 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CaseStudy2', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'News'},
        ),
        migrations.AlterField(
            model_name='news',
            name='type',
            field=models.CharField(max_length=250),
        ),
    ]
