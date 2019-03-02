from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['first_name'])<2:
            errors.append("First name should be more than 2 characters")
        if len(form_data['last_name'])<2:
            errors.append("Last name should be more than 2 characters")
        if not EMAIL_REGEX.match(form_data['email']):
            errors.append("Email should be valid")
        if len(form_data['password']) != len(form_data['confirm_password']):
            errors.append("passwords donot match")
        user_list = self.filter(email=form_data['email'])
        if user_list:
            errors.append("Email already in use")
        return errors
    def create_user(self, form_data):
        # if not self.adminCreated:
        #     self.initAdminFlag()
        # if not self.adminCreated:
        #     user_level = 9
        #     self.adminCreated = True
        # else:
        #     user_level = 0
        hashed_pw=bcrypt.hashpw(form_data['password'].encode(),bcrypt.gensalt())
        
        user=User.objects.create(
            first_name=form_data['first_name'],
            last_name= form_data['last_name'],
            email= form_data['email'],
            password = hashed_pw,
            confirm_password = hashed_pw,
            # user_level = user_level
        )
        return user.id
    def login(self, form_data):
      
        print(form_data)
        errors = []
        existing_users = User.objects.filter (email = form_data['email'])
        if not existing_users:
            return(False, "Email and password not valid")
        user= existing_users[0]
        if bcrypt.checkpw(form_data['password'].encode(), user.password.encode()):
            return(True ,user.id)
        else:
            return (False,"Email and password do not match")   
    # def initAdminFlag(self):
    #     if self.getUserCount() >0:
    #         self.adminCreated = True
    #     else:
    #         self.adminCreated = False
    # def getUserCount(self):
    #     self.all().count()


class User(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password=models.CharField(max_length=255)
    # user_level = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
