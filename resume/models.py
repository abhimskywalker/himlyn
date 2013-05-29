from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt


# Create your models here.
class Template(models.Model):
    user = models.ForeignKey(User)
    resume_type = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default = dt.now())

    def __unicode__(self):
    	return self.user.id


class Category(models.Model):
    section = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default = dt.now())

    def __unicode__(self):
        return self.section


class Title(models.Model):
    template = models.ForeignKey(Template)
    category = models.ForeignKey(Category, default = 1)
    heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default = dt.now())

    def __unicode__(self):
        return self.heading


class Bullet(models.Model):
    title = models.ForeignKey(Title)
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default = dt.now())

    def __unicode__(self):
        return self.content


