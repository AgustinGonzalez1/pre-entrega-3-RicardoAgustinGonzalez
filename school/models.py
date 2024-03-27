from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length = 45)
  course = models.CharField(max_length = 45)
  commission = models.IntegerField()


class Teacher(models.Model):
  name = models.CharField(max_length = 45)
  course_name = models.CharField(max_length = 45)


class Course(models.Model):
  name = models.CharField(max_length = 45)
  teacher = models.CharField(max_length = 45)