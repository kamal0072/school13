from django.shortcuts import render
from .forms import SignUpForm, UserLoginForm, UserChangePwd1, UserChangePwd2
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
#This is user signup Form.
def sign_up(request):
    if request.method=="POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Account created successfully..")
            return HttpResponseRedirect('/signup')
    else:
        fm = SignUpForm()
    return render(request, 'poll/signup.html', {'form' : fm})

#This is user signup Form.
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            fm = UserLoginForm(request=request, data= request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                pwd = fm.cleaned_data['password']
                user = authenticate(username = uname, password = pwd)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You've logged in..")
                    return HttpResponseRedirect('/login')
        else:
            fm = UserLoginForm()
        return render(request, 'poll/login.html', {'form' : fm})
    else:
        return HttpResponseRedirect('/profile')
    
#user profile
def userprofile(request):
    dt = request.user
    print(dt)
    return render(request, 'poll/profile.html', {"user"  : dt})

#user log out view
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/login')


#change user password with old password
def changeuserPassword1(request):
    if request.method=="POST":
        fm = UserChangePwd1(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Password updated successfully..')
            return HttpResponseRedirect('/profile')
    else:
        fm = UserChangePwd1(user=request.user)
    return render(request, 'poll/changepawd1.html', {'form' : fm})

#change user password with new password
def changeuserPassword2(request):
    # if request.user.is_authenticated:
        if request.method=="POST":
            fm = UserChangePwd2(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.info(request, 'New Password set successfully..')
                return HttpResponseRedirect('/profile/')
        else:
            fm = UserChangePwd2(user=request.user)
        return render(request, 'poll/changepawd2.html', {'form' : fm})
    # else:
    #     return HttpResponseRedirect('/login/')