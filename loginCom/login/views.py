from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
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
