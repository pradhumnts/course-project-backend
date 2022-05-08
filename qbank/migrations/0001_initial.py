# Generated by Django 3.2 on 2022-05-03 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=100)),
                ('topicAttribute', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('topic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='system', to='qbank.topic')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.TextField(max_length=5000)),
                ('explanationText', models.TextField(max_length=15000)),
                ('questionHeader', models.CharField(blank=True, max_length=100, null=True)),
                ('isActive', models.BooleanField(default=True)),
                ('hint', models.TextField(blank=True, max_length=500, null=True)),
                ('highlights', models.TextField(blank=True, max_length=1000, null=True)),
                ('correctAnswer', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='qbank.course')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='qbank.section')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='qbank.subject')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='qbank.system')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question', to='qbank.topic')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='sections',
            field=models.ManyToManyField(related_name='course', to='qbank.Section'),
        ),
        migrations.AddField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(related_name='course', to='qbank.Subject'),
        ),
        migrations.AddField(
            model_name='course',
            name='systems',
            field=models.ManyToManyField(related_name='course', to='qbank.System'),
        ),
        migrations.AddField(
            model_name='course',
            name='topics',
            field=models.ManyToManyField(related_name='course', to='qbank.Topic'),
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255)),
                ('answerHeader', models.CharField(blank=True, max_length=200, null=True)),
                ('choiceNumber', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='qbank.question')),
            ],
        ),
    ]
