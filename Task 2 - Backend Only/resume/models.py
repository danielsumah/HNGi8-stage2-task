from django.db import models


# Create your models here.

class Education(models.Model):
    course = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    note = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.school + ' ' + self.course


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name + ' ' + self.subject