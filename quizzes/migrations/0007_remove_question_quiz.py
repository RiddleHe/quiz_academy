# Generated by Django 4.1.3 on 2022-12-17 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0006_alter_score_correct_alter_score_percentage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='quiz',
        ),
    ]