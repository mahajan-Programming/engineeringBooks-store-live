from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserPersonalInfo,NewBook,Calc,WorkShopUniForm,File
from django.forms import ModelForm


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields=['username','first_name','last_name','email','password1','password2']


class UserInfoForm(ModelForm):
    class Meta:
        model= UserPersonalInfo
        fields=['PhoneNo','City','Institute','SubUrb']
            
        


class UserNewBook(ModelForm):
    class Meta:
        model = NewBook
        fields=['BookName','Price','Year','Tag1','Tag2','BookImage']
        labels = {
            'Year':"Book's Publish Year ?",
            'Tag1': "Book's Branch ?"         
            }

class AddCalc(ModelForm):
    class Meta:
        model = Calc
        fields = ['CalcPic','price','modelName']

class AddWorkshopUni(ModelForm):
    class Meta:
        model = WorkShopUniForm
        fields = ['image','size','price']

class AddFile(ModelForm):
    class Meta:
        model=File
        fields=['pdf','Subject_and_Topic','Branch','Semister','Type','Unit']