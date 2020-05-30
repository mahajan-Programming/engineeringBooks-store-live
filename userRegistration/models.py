from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserPersonalInfo(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    PhoneNo = models.CharField(max_length=100,default="")
    City = models.CharField(max_length=20,default="")
    Institute=models.CharField(max_length=50,default="")
    SubUrb=models.CharField(max_length=30,default="")
    def __str__(self):
        return str(self.pk) + '. ' + self.username.username



class NewBook(models.Model):
    BookOwner = models.ForeignKey(UserPersonalInfo,on_delete=models.CASCADE,related_name="owner")
    branch=(('First Year','First Year'),
            ('CSE','CSE'),
            ('IT','IT'),
            ('Entc','Entc'),
            ('Mech','Mech'),
            ('Instrumentation','Instrumentation'),
            ('Production','Production'),
            ('Chemical','Chemical'),
            ('Electrical','Electrical'),
            ('Mechatronix','Mechatronix'),
            )
    semister=(
        ('Sem1','Sem1'),
        ('Sem2','Sem2'),
        ('Sem3','Sem3'),
        ('Sem4','Sem4'),
        ('Sem5','Sem5'),
        ('Sem6','Sem6'),
        ('Sem7','Sem7'),
        ('Sem8','Sem8')
    )    
    BookName=models.CharField(max_length=200,default="")
    Price=models.IntegerField(default=0)
    Year=models.CharField(max_length=10,default="")
    Tag1=models.CharField(max_length=50,choices=branch,default="")
    Tag2=models.CharField(max_length=15,choices=semister,default="")
    BookImage = models.ImageField(blank=True, upload_to='books')
    def __str__(self):
        return str(self.pk) + '. ' + self.BookOwner.username.username+ ' ' + self.BookName


class Calc(models.Model):
    CalcOwner = models.ForeignKey(UserPersonalInfo,on_delete=models.CASCADE,related_name="CalcOwner")
    CalcPic= models.ImageField(blank=True,upload_to='books') 
    price = models.IntegerField(default=0)
    modelName = models.CharField(max_length=20)

class WorkShopUniForm(models.Model):
    CalcOwner = models.ForeignKey(UserPersonalInfo,on_delete=models.CASCADE,related_name="UniformOwner")
    image = models.ImageField(upload_to='books')
    size = models.CharField(max_length=4, default='M')
    price = models.IntegerField(default=100)

#name of pdf choices pdf, mcq ,q-paper, notes,other,price,branch ,semister-->pdf file
class File(models.Model):
    branch = (
            ('All','All'),
            ('First Year','First Year'),
            ('CSE','CSE'),
            ('IT','IT'),
            ('Entc','Entc'),
            ('Mech','Mech'),
            ('Instrumentation','Instrumentation'),
            ('Production','Production'),
            ('Chemical','Chemical'),
            ('Electrical','Electrical'),
            ('Mechatronix','Mechatronix'),
        )
    semister = (
            ('None','None'),
            ('Sem1','Sem1'),
            ('Sem2','Sem2'),
            ('Sem3','Sem3'),
            ('Sem4','Sem4'),
            ('Sem5','Sem5'),
            ('Sem6','Sem6'),
            ('Sem7','Sem7'),
            ('Sem8','Sem8')
        )
    type = (
            ('MCQ','MCQ'),
            ('Q-paper','Q-paper'),
            ('Notes','Notes'),
            ('Decode','Decode'),
            ('Other','Other'),

        )
    unit = (
        ('None','None'),
        ('All','All'),
        ('Unit-1','Unit-1'),
        ('Unit-2','Unit-2'),
        ('Unit-3','Unit-3'),
        ('Unit-4','Unit-4'),
        ('Unit-5','Unit-5'),
        ('Unit-6','Unit-6'),
    )
    pdf = models.FileField(max_length=200,upload_to='books')
    Subject_and_Topic = models.CharField(max_length=40)
    Branch = models.CharField(max_length=40,choices=branch)
    Semister = models.CharField(max_length=40,choices=semister)
    Type = models.CharField(max_length=40,choices=type)
    Unit =  models.CharField(max_length=40,choices=unit)