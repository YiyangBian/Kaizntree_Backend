from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # 导入 Django 的消息框架
# 在你的应用的 views.py 文件中添加
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
                    return redirect('dashboard')  # 使用视图的名称进行重定向
                else:
                    messages.error(request, 'Account is disabled.')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def create_account(request):
    # 你的创建账户的逻辑
    return render(request, 'app/create_account.html')

def recover_password(request):
    # 你的密码恢复的逻辑
    return render(request, 'app/recover_password.html')

def dashboard(request):
    items = Item.objects.all()  # 获取所有项目
    categories = Category.objects.all()  # 获取所有分类
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
        # 如果表单验证失败，你可能需要在此处理其他逻辑
    # 对于GET请求，或者表单验证失败，重定向到仪表板页面
    return redirect('dashboard')

def new_item(request):
    if request.method == 'POST':
        print("POST data:", request.POST)  # 打印前端传来的数据
        form = ItemForm(request.POST)
        # print("Form data:", form.cleaned_data)  # 打印清洗后的表单数据，但这行代码需要放在form.is_valid()之后
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
            return render(request, 'app/dashboard.html', {'form': form})
    else:
        form = ItemForm()
        return render(request, 'app/dashboard.html', {'form': form})

# def search_items(request):
#     if request.method == 'GET':
#         search_query = request.GET.get('search', '')  # 获取搜索栏中的文本
#         print("搜索",search_query)
#         items = Item.objects.filter(name__icontains=search_query) if search_query else Item.objects.all()  # 根据搜索词过滤项目列表
#         categories = Category.objects.all()  # 获取所有分类
#         return render(request, 'app/dashboard.html', {
#             'items': items,
#             'categories': categories,
#             'search_query': search_query,  # 将搜索词传递到模板
#         })
#     else:
#         return redirect('dashboard')  # 如果不是GET请求，重定向到仪表板页面



