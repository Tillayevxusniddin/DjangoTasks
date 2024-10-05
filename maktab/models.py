# models.py
from django.db import models

class Application(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    application_file = models.FileField(upload_to='applications/')

    def __str__(self):
        return self.title
