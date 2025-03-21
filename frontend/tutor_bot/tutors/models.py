from django.db import models

# Create your models here.

class Tutor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    specialization = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    experience = models.IntegerField()

    def __str__(self):
        return self.name

