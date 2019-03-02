from django.db import models
import re 
import bcrypt
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
        print(user.id)
        return user.id
    def login(self, form_data):
        errors=[]
        existing_user = User.objects.filter(email=form_data['email'])
        if not existing_user:
            return (False,"Email or password invalid")
        user = existing_user[0]
        if bcrypt.checkpw(form_data['password'].encode(), user.password.encode()):
            return(True ,user.id)


class BookManager(models.Manager):
    def create_book(self,form_data):
        print("working")
        author_name = form_data['author_first']
        if author_name =="":
            author_name = form_data['author_next']
        print(author_name)
        book=Book.objects.create(
            book_name=form_data['book_name'],
            author =   author_name  

        )
        print("working 3")
        print(book)
        return book.id
    def create_review(self,form_data,book_id,user_id):
        book = Book.objects.get(id= book_id)
        user= User.objects.get(id=user_id)
        review = Review.objects.create(
            review=form_data['review'],
            rating = form_data['stars'],
            book = book,
            reviewed_by= user
           

        ) 
        return review
       
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length= 255)
    confirm_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    
    
class Book(models.Model):
    book_name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Book, related_name="book_reviews")
    reviewed_by = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()