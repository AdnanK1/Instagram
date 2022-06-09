from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def loginPage(request):
    context = {}
    return render(request,'auth/login.html', context)

def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'auth/register.html',context)