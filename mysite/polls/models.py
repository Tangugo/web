from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Question(models.Model):
    """docstring for Question"""
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question_text


class Choice(models.Model):
    """docstring for Choice"""
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def _unicode__(self):
        return self.choice_text
