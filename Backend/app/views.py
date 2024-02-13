from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # 导入 Django 的消息框架
from django.http import HttpResponse
from .forms import LoginForm,CategoryForm,ItemForm
from .models import Item, Category


def home(request):
    return HttpResponse('Welcome to Kaizntree!')



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard') 
                else:
                    messages.error(request, 'Account is disabled.')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def create_account(request):

    return render(request, 'app/create_account.html')

def recover_password(request):

    return render(request, 'app/recover_password.html')

def dashboard(request):
    items = Item.objects.all()  # Get all items
    categories = Category.objects.all()  # Get all categories
    return render(request, 'app/dashboard.html', {
        'items': items,
        'categories': categories
    })

def new_category(request):
    if request.method == 'POST':
        print("POST data:", request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            return render(request, 'app/dashboard.html', {'form': form})
        # If form validation fails, you may need to handle additional logic here
    # For GET requests, or form validation fails, redirect to the dashboard page
    return redirect('dashboard')

def new_item(request):
    if request.method == 'POST':
        print("POST data:", request.POST) 
        form = ItemForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            return render(request, 'app/dashboard.html', {'form': form})
    else:
        form = ItemForm()
        return render(request, 'app/dashboard.html', {'form': form})




