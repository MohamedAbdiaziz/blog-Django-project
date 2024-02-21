from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=210)
    content = models.CharField(max_length=210)
    update = models.DateTimeField(auto_now = True, auto_now_add=False)
    regDate = models.DateTimeField(auto_now = False,auto_now_add=True)

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title