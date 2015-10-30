#coding=utf-8
from django.db import models

# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=200) #问题内容
    pub_date = models.DateTimeField('date published')#发布时间
    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    poll = models.ForeignKey(Poll)#外键 一对多，一端的主键放在多端
    choice_text = models.CharField(max_length=200)# 选项的内容
    votes = models.IntegerField(default=0)#投票数量
    def __unicode__(self):
        return self.choice_text
