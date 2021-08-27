"""wiki URL Configuration

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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path
from wiki_app import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.wiki, name="wiki"),
    path('company<int:id>/', views.detail, name="detail"),
    path('company<int:id>/incoming/', views.incoming, name="incoming"),
    path('company<int:id>/outgoing/', views.outgoing, name="outgoing"),
    path('message<int:id_message>/', views.message, name="message"),
    path('message<int:id_message>/deleted', views.deletemessage, name="deletemessage"),
    path('search/', views.serach_tool, name="search"),

    #Авторизация
    path('signup/', views.signupuser, name="signupuser"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name="loginuser"),

]

urlpatterns += staticfiles_urlpatterns()