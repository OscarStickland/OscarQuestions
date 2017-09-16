from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_title = models.CharField(max_length=200)
    question_text = models.CharField(max_length=1000)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=1000)
    answer_date = models.DateField('date published', default=timezone.now)

    def __str__(self):
        return str(self.question)

class AdminUser(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
