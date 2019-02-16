from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    pass
class Course(models.Model):
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
class Detail(models.Model):
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
