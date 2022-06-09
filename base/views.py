from django.shortcuts import redirect, render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)