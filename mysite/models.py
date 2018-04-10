from django.contrib.auth.models import User
from django.db import models, migrations


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=150)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email)


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    #user = models.ForeignKey(User)

    def __str__(self):
        return self.title
