from django.shortcuts import render
from django.http import Http404

# Create your views here.
def home(request):
    return render(request,'about.html')
from app.models import CreateUserForm
# Create your views here.
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'register.html', context)
def login(request):
    context = {}
    return render(request, 'login.html', context)
