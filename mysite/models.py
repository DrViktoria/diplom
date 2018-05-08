from django.contrib.auth.models import User
from django.db import models, migrations


class UserModel(models.Model):
    f_name = models.CharField(max_length=100, verbose_name=u'Name', null=True)
    l_name = models.CharField(max_length=100, verbose_name=u'L_name', null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.l_name


class Car(models.Model):
    name = models.CharField(max_length=255)


class AlbomModel(models.Model):
    logo =models.ImageField()
    named = models.CharField(max_length=50)
    discription_albom = models.TextField (max_length=100)


class ImageModel(models.Model):
    img = models.ImageField()
    note = models.TextField(max_length=250)
    result = models.CharField(max_length=50)

