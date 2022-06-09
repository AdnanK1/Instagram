from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Image,Profile

# Create your views here.
@login_required(login_url='login')
def home(request):
    images = Image.objects.all()
    context = {'images':images }
    return render(request, 'home.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
    context = {}
    return render(request,'auth/login.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            form.save()
            login(request,user)
            return redirect('home')
    context = {'form':form}
    return render(request,'auth/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')