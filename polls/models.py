from __future__ import unicode_literals

from django.db import models

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200, default='SOME STRING')
    apellido = models.CharField(max_length=200, default='SOME STRING')
    comentario = models.CharField(max_length=200, default='SOME STRING')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
