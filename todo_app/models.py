from django.db import models
from django.contrib.auth.models import User


class task(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    complete=models.BooleanField(default=False)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

