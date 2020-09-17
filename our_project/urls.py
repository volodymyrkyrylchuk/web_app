"""our_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from accounts.views import get_profiles_list, get_profile, add_profile, edit_profile, get_publication

urlpatterns = [
    path('', get_profiles_list),
    path('admin/', admin.site.urls),
    path('profiles/', get_profiles_list),
    path('profiles/add/', add_profile),
    path('profiles/show/<slug>', get_profile),
    path('profiles/edit/<slug>', edit_profile),
    path('publication/show/<id>', get_publication),
    
]
