from django.db import models

# Create your models here.
class Student(models.Model):
    def __str__(self):
        return self.sid
    sid = models.CharField(max_length=10,unique=True)



