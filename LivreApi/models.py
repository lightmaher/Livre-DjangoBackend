from django.contrib.auth.models import AbstractUser
from django.db import models

#Livre_Project_Models
def upload_to(instance, filename):
    return 'book/{filename}'.format(filename=filename)
def upload_toprofile(instance, filename):
    return 'profile/{filename}'.format(filename=filename)


#User_Model
class User(AbstractUser):   
    is_blocked = models.BooleanField(default=False , null = True)
    is_admin = models.BooleanField(default=False , null = True)
    image = models.ImageField(upload_to=upload_toprofile , default='profile/def.jpg' )
    user_gender = (("Male", "Male"), ("Female", "Female"))
    gender = models.CharField(max_length= 6, choices=user_gender,null = True)
    date_of_birth = models.DateField(null = True)
    country = models.CharField(max_length = 200,null = True)
    location = models.CharField(max_length = 200,null = True)
    phone = models.CharField(max_length = 20,null = True)
    email = models.EmailField(verbose_name = 'email',max_length=50, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

#Category_Model
class Category(models.Model):
    name = models.CharField(max_length=50,null=True) 
    image = models.ImageField(upload_to=upload_to, null=True , default='book/default-book.png')
    # cat_picture = models.ImageField(null=True, blank=True , upload_to="img/" ,default='img/Default_Image.png')
    def __str__(self):
        return self.name

#Subscription_Model
class Subscription(models.Model):
    cat = models.ForeignKey(Category, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    def __str__(self):
        return self.cat.name

#Book_Model
class Book(models.Model):
    title=models.CharField(max_length=50, null=True)
    author=models.CharField(max_length=50,null=True )
    image = models.ImageField(upload_to=upload_to, null=True , default='book/default-book.png')
    description = models.TextField(null=True)
    book_status = (("Exchange", "Exchange"), ("Donate", "Donate"))
    status = models.CharField(max_length= 20, choices=book_status,null = True)
    date_creation = models.DateTimeField(auto_now_add=True , null = True)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    cat = models.ForeignKey(Category, on_delete= models.CASCADE)
    def __str__(self):
        return self.title

#Transaction_Model
class Transaction(models.Model):
    is_accepted = models.BooleanField(default=False,null=True)
    sender_finished = models.BooleanField(default=False,null=True)
    receiver_finished = models.BooleanField(default=False,null=True)
    date_creation = models.DateTimeField(auto_now_add=True , null = True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
    tr_sender = models.ForeignKey(User,related_name ="tr_sender", on_delete= models.CASCADE)
    tr_receiver = models.ForeignKey(User,related_name="tr_receiver", on_delete= models.CASCADE)
    def __str__(self):
        return self.book.title

#Message_Model
class Message(models.Model):
    content = models.CharField(max_length=250,null= True)
    date_creation = models.DateTimeField(auto_now_add=True , null = True)
    m_sender = models.ForeignKey(User,related_name ="m_sender", on_delete= models.CASCADE)
    m_receiver = models.ForeignKey(User,related_name="m_receiver", on_delete= models.CASCADE)    
    def __str__(self):
        return self.content

#Rate_Model
class Rate(models.Model):
    user_rate = (("1", 1), ("2", 2),("3",3),("4",4),("5",5))
    rate = models.CharField(max_length= 10, choices=user_rate,null = True)
    r_sender = models.ForeignKey(User,related_name ="r_sender", on_delete= models.CASCADE)
    r_receiver = models.ForeignKey(User,related_name="r_receiver", on_delete= models.CASCADE)      
    def __str__(self):
        return self.rate

