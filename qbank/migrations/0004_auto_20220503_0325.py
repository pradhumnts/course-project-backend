# Generated by Django 3.2 on 2022-05-03 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qbank', '0003_alter_course_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='system',
            field=models.ManyToManyField(blank=True, related_name='subject', to='qbank.System'),
        ),
        migrations.AlterField(
            model_name='course',
            name='topics',
            field=models.ManyToManyField(blank=True, related_name='course', to='qbank.Topic'),
        ),
    ]