from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['name'])<6:
            errors. append("Course name should be more than 5 characters")
        if len(form_data['description'])<15:
            errors. append("Description should be more than 15 characters")
        
        return errors
    def create_course(self, form_data):
        print(form_data['name'])
        return self.create(
            name=form_data['name'],
            desc = form_data['description']
        )
    
        
class Course(models.Model):
    name = models.CharField(max_length=255)
    desc = models.OneToOneField(Detail)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()
class Detail(models.Model):
    desc = models.TextField()