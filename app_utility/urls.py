"""TextUtility URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url,include
from app_utility.views import perform_utility

app_name = 'app_utility'
urlpatterns = [
    url(r'(?P<utility_type>.+)$',perform_utility,name="utility"),
    #path('textstats/',perform_stats),
    #path('removechar/',perform_removeChar),
    #path('specialchar/',perform_specialChar),
    
]
