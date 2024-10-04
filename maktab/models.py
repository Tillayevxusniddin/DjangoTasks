

from django.db import models
from django.contrib.auth.models import User
#
#
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     location = models.CharField(max_length=100, blank=True)
#
#     def __str__(self):
#         return f'{self.user.username} Profile'
#
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class StudentManager(models.Manager):
    def adults(self):
        return self.filter(age__gte=18)

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    courses = models.ManyToManyField(Course)

    objects = StudentManager()
    def __str__(self):
        return self.name



########################

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def word_count(self):
        return len(self.description.split())

    def __str__(self):
        return self.title





