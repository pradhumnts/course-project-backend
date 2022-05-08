# Generated by Django 3.2 on 2022-05-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='topic',
        ),
        migrations.AddField(
            model_name='system',
            name='topic',
            field=models.ManyToManyField(related_name='system', to='qbank.Topic'),
        ),
    ]
