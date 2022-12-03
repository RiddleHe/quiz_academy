from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Quiz(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):

    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200, null=True)
    quiz = models.ForeignKey(Quiz, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Score(models.Model):

    created_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "Score"
