# Generated by Django 3.2 on 2022-05-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbank', '0004_auto_20220503_0325'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='subject',
            field=models.ManyToManyField(blank=True, to='qbank.Subject'),
        ),
    ]