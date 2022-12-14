# Generated by Django 4.1.3 on 2022-12-17 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0007_remove_question_quiz'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='curr_question',
        ),
        migrations.AddField(
            model_name='question',
            name='next_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.question'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='head',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quizzes.question'),
        ),
    ]
