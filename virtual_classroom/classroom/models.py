from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    enrolled_classes = models.ManyToManyField('Class', related_name='students')

class Class(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

class Unit(models.Model):
    class_room = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='units')
    title = models.CharField(max_length=255)

class Session(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=255)
    description = models.TextField()

class Lecture(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=255)
    content = models.TextField()

class Discussion(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='discussions')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
