from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['first_name'])<3:
            errors. append("First name should be more than 2 characters")
        if len(form_data['last_name'])<3:
            errors. append("Last name should be more than 2 characters")
        if not EMAIL_REGEX.match(form_data['email']):
            errors. append("Email must be valid")
        user_list = self.filter(email=form_data['email'])
        if user_list:
            errors.append("Email already in use")
        return errors
    def create_user(self, form_data):
        return self.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email']
        )
    def edit_user(self, form_data):
        self.user = User.objects.get(id=id)
        self.user.first_name=form_data['first_name'],
        self.user.last_name=form_data['last_name'],
        self.user.email=form_data['email'],
        self.user.save()
        return self.user

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()