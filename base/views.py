from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Image,Profile
from .forms import PostForm,ProfileForm

# Create your views here.
@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    images = Image.objects.filter(
        Q(caption__icontains=q) 
    )
    profiles = Profile.objects.all()
    context = {'images':images,'profiles':profiles }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def createPost(request):
    form = PostForm()
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'createPost.html', context)

@login_required(login_url='login')
def profilePage(request):
    form = ProfileForm()
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'profile.html', context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist ')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {'page':page}
    context = {}
    return render(request,'auth/login.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = form.save()
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    context = {'form':form}
    return render(request,'auth/register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')