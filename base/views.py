from django.shortcuts import render,redirect
from .forms import CreateUserForm

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def loginPage(request):
    context = {}
    return render(request,'auth/login.html', context)

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'auth/register.html',context)