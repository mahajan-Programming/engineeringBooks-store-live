from django.shortcuts import render,redirect, HttpResponse
from .models import UserPersonalInfo,NewBook,User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
import uuid 
Merchant_Key = "HiH%!dJxlr5ivoPB"
# Create your views here.
def index(request):
    a=0
    name = 'anonymous'
    if request.method== 'POST':
        param_dict = {
                    "MID": "qsOMNF52276719267774",
                    "ORDER_ID": str(uuid.uuid1()) ,
                    "CUST_ID": "shreyashpm@gmail.com",
                    "TXN_AMOUNT": "100",
                    "CHANNEL_ID": "WEB",
                    "INDUSTRY_TYPE_ID": "Retail",
                    "WEBSITE": "WEBSTAGING",
                    'CALLBACK_URL': "http://127.0.0.1:8000/handlerequest/"
            }
        param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict, Merchant_Key)
        return render(request,"paytm.html",{'param_dict':param_dict})
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

        

       
        return render(request,"newcardpage.jinja",{'books':books,'b':branch,'s':sem,'a':1})
    return render(request,"newsearchpage.html",{})

def books(request):
    return render(request,"bookscardpage.html",{})

def newbooks(request):
    return render(request,"newcardpage.jinja",{})

def NewSearch(request):
    return render(request,"newsearchpage.html",{})

A=0
@login_required
def sellerDashBoard(request):
    global A
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
            A=NewBook.objects.get(pk=soldBook)
            param_dict = {
                    "MID": "qsOMNF52276719267774",
                    "ORDER_ID": str(uuid.uuid1()) ,
                    "CUST_ID": "shreyashpm@gmail.com",
                    "TXN_AMOUNT": "100",
                    "CHANNEL_ID": "WEB",
                    "INDUSTRY_TYPE_ID": "Retail",
                    "WEBSITE": "WEBSTAGING",
                    'CALLBACK_URL': "http://127.0.0.1:8000/handlerequest/"
            }
            param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict, Merchant_Key)

            return render(request,"paytm.html",{'param_dict':param_dict})
        except:
            pass
        try:
            soldcalc = request.POST.get('soldclac')
            A = Calc.objects.get(pk=soldcalc)
            param_dict = {
                    "MID": "qsOMNF52276719267774",
                    "ORDER_ID": str(uuid.uuid1()) ,
                    "CUST_ID": "shreyashpm@gmail.com",
                    "TXN_AMOUNT": "100",
                    "CHANNEL_ID": "WEB",
                    "INDUSTRY_TYPE_ID": "Retail",
                    "WEBSITE": "WEBSTAGING",
                    'CALLBACK_URL': "http://127.0.0.1:8000/handlerequest/"
            }
            param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict, Merchant_Key)
            return render(request,"paytm.html",{'param_dict':param_dict})

        except:
            pass
        try:
            solduni = request.POST.get('solduni')
            A=WorkShopUniForm.objects.get(pk=solduni)
            param_dict = {
                    "MID": "qsOMNF52276719267774",
                    "ORDER_ID": str(uuid.uuid1()) ,
                    "CUST_ID": "shreyashpm@gmail.com",
                    "TXN_AMOUNT": "100",
                    "CHANNEL_ID": "WEB",
                    "INDUSTRY_TYPE_ID": "Retail",
                    "WEBSITE": "WEBSTAGING",
                    'CALLBACK_URL': "http://buy-n--sell.herokuapp.com/handlerequest/"
            }
            param_dict["CHECKSUMHASH"] = Checksum.generate_checksum(param_dict, Merchant_Key)
            return render(request,"paytm.html",{'param_dict':param_dict})

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

@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict ={}
    for i in form.keys():
        response_dict[i] = form[i]
        if i== 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, Merchant_Key, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print("order succesful")
            A.delete()
        else:
            print("order not successful because"+ response_dict["RESPMSG"])
    return render(request,"paymentstatus.html",{"response":response_dict})

