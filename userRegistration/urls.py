from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings

from django.conf.urls.static import static

from . import views 
from userRegistration.views import index,register,userInfoFrom,NewBookForm,Test,books,newbooks,NewSearch,sellerDashBoard,CalcForm,Uniform,UniCard,FileForm,ShowFileFolder

urlpatterns = [
    path('', views.index, name='index'),
    path('register/',views.register,name='registerform'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html'),name="loginform"),
    path('logout/',auth_views.LogoutView.as_view(template_name='logout.html'),name="logout"),
    path('userinfo/',views.userInfoFrom,name="userinfoform"),
    path('newbook/',views.NewBookForm,name="newbookform"),
    path('searchbooks/',views.Test,name="searchbooks"),
    path('books/',views.books,name="search"),
    path('newbooks/',views.newbooks,name="newbooks"),
    path('sellerdash/',views.sellerDashBoard,name="sellerdash"),
    path('calcform/',views.CalcForm, name="calcform"),
    path('Uniform/',views.Uniform, name="Uniform"),
    path('Uniformcards/',views.UniCard,name="unicards"),
    path('FileForm/',views.FileForm,name="FileForm"),
    path('ShowFileFolder/<str:branch>/',views.ShowFileFolder,name="filesFolder")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
