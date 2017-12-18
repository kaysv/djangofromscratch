from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

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
