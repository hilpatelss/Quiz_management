"""
URL configuration for quiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import *
from parents.views import *
from institute.views import *

urlpatterns = [
    # common    
    path('aboutus/' , aboutus , name="aboutus"), 
    path('feedback/' , feedback , name="feedback"),

    # student
    path('admin/', admin.site.urls),
    path('' , home , name="home"),
    path('home/' , home , name="home"),
    path('chapter/<str:data>/' , chapter , name="chapter"),
    path('subject/<str:data>/' , subject , name="subject"),
    path('exam/' , exam , name="exam"),
    path('result/' , result , name="result"),
    path('score/' , score , name="score"),
    path('test/<str:data>/' , test , name="test"),
    path('forget_1/' , forget_1 , name="forget_1"),
    path('forget_2/<str:data>/' , forget_2 , name="forget_2"),
    path('otp/' , otp , name="otp"),
    path('profile/' , profile , name="profile"),
    path('signin/' , signin , name="signin"),
    path('signup/' , signup , name="signup"),
    path('signout/' , signout , name="signout"),
    path('guardian_edit/' , guardian_edit , name="guardian_edit"),
    path('guardian_view/' , guardian_view , name="guardian_view"),
    # parents
    path('parents/' , p_home , name="p_home"),
    path('parents/score/' , p_score , name="p_score"),
    path('parents/forget_1/' , p_forget_1 , name="p_forget_1"),
    path('parents/forget_2/' , p_forget_2 , name="p_forget_2"),
    path('parents/otp/' , p_otp , name="p_otp"),
    path('parents/profile/' , p_profile , name="p_profile"),
    path('parents/signin/' , p_signin , name="p_signin"),
    path('parents/signup/' , p_signup , name="p_signup"),
    # institue
    path('institute/' , i_home , name="i_home"),
    path('institute/score/' , i_score , name="i_score"),
    path('institute/forget_1/' , i_forget_1 , name="i_forget_1"),
    path('institute/forget_2/' , i_forget_2 , name="i_forget_2"),
    path('institute/otp/' , i_otp , name="i_otp"),
    path('institute/profile/' , i_profile , name="i_profile"),
    path('institute/signin/' , i_signin , name="i_signin"),
    path('institute/signup/' , i_signup , name="i_signup"),
]
