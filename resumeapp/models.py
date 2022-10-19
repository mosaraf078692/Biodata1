from django.db import models

# Create your models here.

class namedatas(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    number=models.CharField(max_length=50)
    message=models.TextField(max_length=50)
    date=models.DateTimeField()

    def __str__(self):
        return self.name