from django.shortcuts import redirect
from django.contrib.auth import authenticate, logout, login

def login_view(request):
    if request.method  == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)

    return redirect('/')

def logout_view(request):
    logout(request)
    if request.GET['next']:
        return redirect(request.GET['next'])
    
    return redirect('/')