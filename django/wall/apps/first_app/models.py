from django.db import models
import re
import bcrypt

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
        hashed_pw=bcrypt.hashpw(form_data['password'].encode(),bcrypt.gensalt())
        print(hashed_pw)
        
        user= User.objects.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            password=hashed_pw
                 
        )
        print(user.id)
        return user.id
    def login(self,form_data):
        print(form_data)
        errors = []
        existing_users = User.objects.filter(email=form_data['email'])
        print (existing_users)
        if not existing_users:
            return(False, "Email or password invalid")
        user = existing_users[0]
        if bcrypt.checkpw(form_data['password'].encode(), user.password.encode()):
            return(True ,user.id)
            
        else:
            return (False,"Email and password do not match")   
    def create_message(self,form_data,user_id):
        print("this is form_data", form_data)
        user = User.objects.get(id=user_id)
        new_message = Message.objects.create(
            message= form_data['description'],
            messager= user
        )
        print('*'* 30, new_message)
        return new_message
    def create_comment(self,form_data,user_id,message_id):
        print("this is comment form_data", form_data)
        user = User.objects.get(id=user_id)
        comments = Message.objects.get(id=form_data['message_id'])
        
               
        new_comment = Comment.objects.create(
            comment= form_data['comment'],
            creator= user,
            post= comments
        )
        print('*'* 30, new_comment)
        return new_comment
        

class User(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
class Message(models.Model):
    message = models.TextField()
    messager = models.ForeignKey(User,related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Comment(models.Model):
    comment = models.TextField()
    creator = models.ForeignKey(User,related_name="user")
    post = models.ForeignKey(Message,related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


