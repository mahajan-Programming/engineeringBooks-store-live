from django.shortcuts import render,redirect
from .models import UserPersonalInfo,NewBook
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    a=0
    name = 'anonymous'
    try:
       name = UserPersonalInfo.objects.get(username= request.user)
    except:
        a=1
    return render(request,"index.html",{'check':a,'n':name})

from .forms import RegisterForm,UserInfoForm,UserNewBook,AddCalc,AddWorkshopUni,AddFile
from userRegistration.models import Calc, File, WorkShopUniForm


# Create your views here.
def register(request):
    if request.method == "POST":
	    form = RegisterForm(request.POST)

	    if form.is_valid():
	        form.save()

	    return redirect("index")
    else:
	    form = RegisterForm()

    return render(request, "register.html", {"form":form})


@login_required
def userInfoFrom(request):
    userinfo=UserInfoForm(request.POST)
    if request.method == 'POST':
        user = userinfo.save(commit=False)
        user.username=request.user
        userinfo.save()
        return redirect('sellerdash')
    return render(request,"UserInfoForm.html",{'userinfo':userinfo})

@login_required
def NewBookForm(request):
    new = UserNewBook(request.POST,request.FILES)
    if request.method == 'POST':
        n=  new.save(commit=False)
        current_user= UserPersonalInfo.objects.get(username=request.user)
        n.BookOwner=current_user
        new.save()
        return redirect('sellerdash')

    return render(request,"NewBook.html",{'new':new})

def Test(request):
    if request.method=='POST':
        branch=request.POST.get('branch')
        sem=request.POST.get('sem')
        books =  NewBook.objects.filter(Tag1=branch,Tag2=sem)
        return render(request,"newcardpage.html",{'books':books,'b':branch,'s':sem})
    return render(request,"newsearchpage.html",{})

def books(request):
    return render(request,"bookscardpage.html",{})

def newbooks(request):
    return render(request,"newcardpage.html",{})

def NewSearch(request):
    return render(request,"newsearchpage.html",{})


@login_required
def sellerDashBoard(request):
    current_user = UserPersonalInfo.objects.get(username = request.user)
    current_user_books =  NewBook.objects.filter(BookOwner = current_user)
    current_user_calc = Calc.objects.filter(CalcOwner = current_user)
    current_user_uni = WorkShopUniForm.objects.filter(CalcOwner = current_user)
    if request.method == 'POST':
        soldBook = request.POST.get('sold')
        NewBook.objects.get(pk=soldBook).delete()
        soldcalc = request.POST.get('soldclac')
        Calc.objects.get(pk=soldcalc).delete()
        solduni = request.POST.get('solduni')
        WorkShopUniForm.objects.get(pk=solduni).delete()
    return render(request,"sellerdashboard.html",{'books':current_user_books,'current_user_calc':current_user_calc,'uniform':current_user_uni})


def CalcForm(request):
    new = AddCalc(request.POST,request.FILES)
    if request.method == 'POST':
        n=  new.save(commit=False)
        current_user= UserPersonalInfo.objects.get(username=request.user)
        n.CalcOwner=current_user
        new.save()
        return redirect('index')
    return render(request,'CalcForm.html',{'new':new})


def Uniform(request):
    new = AddWorkshopUni(request.POST,request.FILES)
    if request.method == 'POST':
        n=  new.save(commit=False)
        current_user= UserPersonalInfo.objects.get(username=request.user)
        n.CalcOwner=current_user
        new.save()
        return redirect('index')
    return render(request,'AddUniform.html',{'new':new})

def UniCard(request):
    uniform = WorkShopUniForm.objects.all()
    calculator = Calc.objects.all()
    return render(request,"uniformcards.html",{'uniform':uniform,'calculator':calculator})

def FileForm(request):
    new = AddFile(request.POST,request.FILES)
    if request.method == 'POST':
        new.save()
        return redirect('index')

    return render(request,"FileForm.html",{'new':new})

def ShowFileFolder(request,branch):
    files = File.objects.all()
    return render(request,"FileFolder.html",{'branch':branch,'files':files})