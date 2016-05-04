#! coding = utf-8

from __future__ import unicode_literals

import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class Question(models.Model):
    """docstring for Question"""
    question_text = models.CharField('question text', max_length=200)
    pub_date = models.DateTimeField('published date')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    class Mate():
        db_table = 'question'

class Choice(models.Model):
    """docstring for Choice"""
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
