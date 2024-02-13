"""Backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import user_login,create_account,recover_password, dashboard,new_category,new_item  # 确保导入了你的视图
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect


# 定义一个用于重定向的视图函数，这样做比使用 lambda 函数更清晰
def redirect_to_login(request):
    return redirect('login/', permanent=False)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),  # 登录页面的 URL 没有改变
    path('', redirect_to_login),  # 使用视图函数重定向根 URL 到登录页面
    path('create_account/', create_account, name='create_account'),
    path('recover_password/', recover_password, name='recover_password'),
    path('dashboard/', dashboard, name='dashboard'),
    path('new_category/', new_category, name='new_category'),
    path('new_item/', new_item, name='new_item'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
