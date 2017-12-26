from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import time
from .forms import SignUpForm

# Create your views here.
def dealDjangoForm(request):
    signUpForm = SignUpForm()
    context = {'signUpForm':signUpForm}

    if request.method == "POST":
        signup = SignUpForm(request.POST)
        if signup.is_valid():
            user = signup.save(commit=False)
            user.is_active = True
            user.save()
        else:
            print(signup.error_messages)

        return HttpResponse(dict(request.POST))

    return render(request,"login/djangoform.html",context)


def homeView(request):

    return render(request,'login/login_page.html',{})

def dealLogin(request):
    if request.method == 'POST':
        print('is data here')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # checking if user exist
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    return redirect('/')

def dealLogout(request):
    logout(request)
    return redirect('/')

def dealReg(request):
    if request.method == 'POST':
        if request.POST.get('LoginType') == 'SignIn':
            username = request.POST.get('username')
            password = request.POST.get('password')
            # checking if user exist
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return render(request,'login/regLog.html',{})
        elif request.POST.get('LoginType') == 'SignUp':
            # Registration block
            print(request.POST)
            # user = User.objects.create_user(username='john',
            #                      email='jlennon@beatles.com',
            #                      password='glass onion')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            username = request.POST.get('username')
            if pass1 != pass2:
                return HttpResponse('PASSWORD MATCH GARENA')
            else:
                user = User.objects.create_user(username=username,
                                                first_name = firstname,
                                                last_name = lastname,
                                                email=email,
                                                password=pass1)
                user.save()
                return HttpResponse('save gariyo')
            return HttpResponse(request.POST)
        else:
            pass
    return render(request,'login/regLog.html',{})


def dealVerifyUser(request):
    time.sleep(3)
    if request.method=="POST":
        if request.POST.get("loginType")=="check_user_exist":
            print(request.POST.get("username"))
            if User.objects.filter(username=request.POST.get("username")):
                return HttpResponse("failure")
            else:
                return HttpResponse("success")
    return redirect("/")

def dealAjaxReg(request):
    time.sleep(4)
    if request.method=="POST":
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        print(
                'firstname :'+ firstname + \
                'lastname :' + lastname + \
                'password :' + pass1 + \
                'email :' + email +\
                'username :' + username
                )
        # user = User.objects.create_user(username=username,
        #                                 first_name = firstname,
        #                                 last_name = lastname,
        #                                 email=email,
        #                                 password=pass1)
        # user.save()
        return HttpResponse('success')
    return redirect('/')
