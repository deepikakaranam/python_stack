from django.db import models
import re 
import bcrypt

# Create your models here.


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['first_name'])<2:
            errors.append("first name should be more than 2 characters")
        if len(form_data['last_name'])<2:
            errors.append("Last name should be more than 2 characters")
        if len(form_data['password'])<8:
            errors.append("Password should be more than 8 characters")
        if len(form_data['password'])!= len(form_data['confirm_password']):
            errors.append("Passwords donot match")

        if not EMAIL_REGEX.match(form_data['email']):
            errors.append("Email must be valid")
        user_list = User.objects.filter(email=form_data['email'])
        if user_list:
            errors.append("Email already exits")
        return errors
    def create_user(self, form_data):
        hashed_pw=bcrypt.hashpw(form_data['password'].encode(),bcrypt.gensalt())
        print(hashed_pw)
        hashed_confirm=bcrypt.hashpw(form_data['confirm_password'].encode(),bcrypt.gensalt())
        
        user= User.objects.create(
            first_name=form_data['first_name'],
            last_name=form_data['last_name'],
            email=form_data['email'],
            password=hashed_pw,
            confirm_password=hashed_confirm
                 
        )
        print("working", user)
        return user.id
    def login(self, form_data):
        errors=[]
        existing_user = User.objects.filter(email=form_data['email'])
        if not existing_user:
            return (False,"Email or password invalid")
        user = existing_user[0]
        print(user)
        if bcrypt.checkpw(form_data['password'].encode(), user.password.encode()):
            return(True ,user.id)
class JobManager(models.Manager):
    def validate(self, form_data):
        errors = []
        if len(form_data['title'])<3:
            errors.append("Title should be more than 3 characters")
        if len(form_data['location'])<1:
            errors.append("Location should not be blank")
        if len(form_data['description'])<10:
            errors.append("description should be more than 10 characters")
               
        return errors
    def create_job(self, form_data,user_id):
        user = User.objects.get(id=user_id)
        job= Job.objects.create(
            title = form_data['title'],
            location = form_data['location'],
            description = form_data['description'],
            user= user
                 
        )
        print("working", job)
        return job.id   

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length= 255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Job(models.Model):
    title = models.CharField(max_length = 255)
    location = models.CharField(max_length = 255)
    user = models.ForeignKey(User, related_name="user_jobs")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = JobManager()

