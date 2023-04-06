"""book URL Configuration

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
from app1 import views

from user import views as data_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home_page"),
    path('book-store/', views.store_books, name="store_books"),
    path('update-book/<int:id>/', views.update_book, name="update_book"),
    path('delete-book/<int:id>/', views.delete_book, name="delete_book"),
    path('soft-book/<int:id>/', views.soft_delete, name="soft_delete"),
    path('inactive-store/', views.inactive_books, name="inactive_books"),
    path('restore-store/<int:id>/', views.restore_book, name="restore_book"),
    path('register/', data_views.register_request , name="register_page"),
    path('simple-login/', data_views.login_request , name="login_request"),
    path('logout/', data_views.logout_request , name="logout_request"),




]
