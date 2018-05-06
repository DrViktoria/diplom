from django.contrib.auth.models import User
from django.db import models, migrations


class UserModel(models.Model):
    f_name = models.CharField(max_length=100, verbose_name=u'Name', null=True)
    l_name = models.CharField(max_length=100, verbose_name=u'L_name', null=True)
    user = models.OneToOneField(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.l_name


