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
        labels={
            'username':'Username as "Yourname and Birthdate" ....for ex.--> "  jhon07-03-2000  " ',
        }

class UserInfoForm(ModelForm):
    class Meta:
        model= UserPersonalInfo
        fields=['PhoneNo','City','Institute','SubUrb']
        labels={
            'SubUrb':"Your Area/Locality/Chowk"
        }
        


class UserNewBook(ModelForm):
    class Meta:
        model = NewBook
        fields=['BookName','Price','Year','Tag1','Tag2','BookImage']
        labels = {
            'Year':"Book's Publish Year ?",
            'Tag1': "Book's Branch ?"       ,
            'Tag2': "Semister"  ,
            'BookName':"Book Name",
            'BookImage':"Book Image",
            }

class AddCalc(ModelForm):
    class Meta:
        model = Calc
        fields = ['CalcPic','price','modelName']
        labels={
            'CalcPic': "Calculator Picture",
            'modelName': "Model Name",
            'price':"Price"
        }
class AddWorkshopUni(ModelForm):
    class Meta:
        model = WorkShopUniForm
        fields = ['image','size','price']
        labels={
            'image':"Labcoat Picture",
            'size':"Size",
            'price':"Price"
        }

class AddFile(ModelForm):
    class Meta:
        model=File
        fields=['pdf','Subject_and_Topic','Branch','Semister','Type','Unit']
