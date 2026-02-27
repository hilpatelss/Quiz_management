from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.


def i_home(request):
    contact = {'page': 'i_Home'}
    return  redirect('/home')
    #    return render(request , "core/home.html", contact)

def i_score(request):
    contact = {'page': 'i_score'}
    return  redirect('/home')
    #    return render(request , "test/i_score.html", contact)

def i_forget_1(request):
    contact = {'page': 'i_forget_1'}
    return  redirect('/home')
    #    return render(request , "user/i_forget_1.html", contact)

def i_forget_2(request):
    contact = {'page': 'i_forget_2'}
    return  redirect('/home')
    #    return render(request , "user/i_forget_2.html", contact)

def i_otp(request):
    contact = {'page': 'i_otp'}
    return  redirect('/home')
    #    return render(request , "user/i_otp.html", contact)

def i_profile(request):
    contact = {'page': 'i_profile'}
    return  redirect('/home')
    #    return render(request , "user/i_profile.html", contact)

def i_signin(request):
    contact = {'page': 'i_signin'}
    return  redirect('/home')
    #    return render(request , "user/i_signin.html", contact)

def i_signup(request):
    contact = {'page': 'i_signup'}
    return  redirect('/home')
    #    return render(request , "user/i_signup.html", contact)
