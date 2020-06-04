from django.shortcuts import render,redirect
from .models import UserPersonalInfo,NewBook,User
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
	        new_user=form.save()
            
            # username = form.cleaned_data['username']
            # if User.objects.filter(username=username).exists():
            #     context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
            #     return render(request, "register.html", context)
        
	    return redirect("index")
    else:
	    form = RegisterForm()

    return render(request, "register.html", {"form":form})


@login_required
def userInfoFrom(request):
    information=0
    try:
        information=UserPersonalInfo.objects.get(username=request.user)
    except:
        pass
    userinfo=UserInfoForm(request.POST)
    if request.method == 'POST':
        user = userinfo.save(commit=False)
        user.username=request.user
        userinfo.save()
        return redirect('sellerdash')
    return render(request,"UserInfoForm.html",{'userinfo':userinfo,'info':information})

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
    try:
        if(UserPersonalInfo.objects.all()):
            current_user = UserPersonalInfo.objects.get(username = request.user)

    except:
        userinfo=UserInfoForm(request.POST)
        if request.method == 'POST':
            user = userinfo.save(commit=False)
            user.username=request.user
            userinfo.save()
            return redirect('sellerdash')
        return render(request,"UserInfoForm.html",{'userinfo':userinfo})
    current_user_books =  NewBook.objects.filter(BookOwner = current_user)
    current_user_calc = Calc.objects.filter(CalcOwner = current_user)
    current_user_uni = WorkShopUniForm.objects.filter(CalcOwner = current_user)
    try:
        if(UserPersonalInfo.objects.all()):
            pass
    except:
        return render(request,)
    if request.method == 'POST':
        try:
            soldBook = request.POST.get('sold')
            NewBook.objects.get(pk=soldBook).delete()
        except:
            pass
        try:
            soldcalc = request.POST.get('soldclac')
            Calc.objects.get(pk=soldcalc).delete()
        except:
            pass
        try:
            solduni = request.POST.get('solduni')
            WorkShopUniForm.objects.get(pk=solduni).delete()
        except:
            pass
    return render(request,"newsellerdashboard.html",{'books':current_user_books,'current_user_calc':current_user_calc,'uniform':current_user_uni})


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

def Test12(request):
    return render(request,"allcardsofseller.html",{})


