from django.contrib.auth.models import User
from django.db import models


class UserBalance(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    pic = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return str(self.name)

