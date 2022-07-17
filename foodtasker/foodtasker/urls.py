"""foodtasker URL Configuration

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
from coreapp import views
from django import urls
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('restorant/', views.restorant_home,name='restorant_home'),
    path('restorant/sign_up/', views.restorant_sign_up,name='restorant_sign_up'),

    path('restorant/sign_in/', auth_views.LoginView.as_view(template_name='restorant/sign_in.html'),name='restorant_sign_in'),
    path('restorant/sign_out/', auth_views.LogoutView.as_view(next_page='/'),name='restorant_sign_out'),

]
