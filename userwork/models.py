from django.db import models


# Create your models here.

class Message(models.Model):
    msg = models.CharField(max_length=400)

    def __str__(self):
        return self.msg