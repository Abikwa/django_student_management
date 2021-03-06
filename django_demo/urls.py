"""django_demo URL Configuration

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

from django.conf.urls import url, handler404

import django_demoapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', django_demoapp.views.home, name="home"),
    path('responsibles/', django_demoapp.views.responsibles, name="responsibles"),
    path('responsibles/<int:responsible_id>/delete/', django_demoapp.views.responsibledelete, name="responsibledelete"),
    path('responsibles/<int:responsible_id>/', django_demoapp.views.detail, name="detail"),
    
    path('courses/<int:course_id>/', django_demoapp.views.coursedelete, name="coursedelete"),
    path('courses/', django_demoapp.views.courses, name="courses"),
]
handler404 = 'django_demoapp.views.error_404_view'