"""mysite URL Configuration

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
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('404/', TemplateView.as_view(template_name='404.html'), name='404'),
    path('blank/', TemplateView.as_view(template_name='blank.html'), name='blank'),
    path('buttons/', TemplateView.as_view(template_name='buttons.html'), name='buttons'),
    path('cards/', TemplateView.as_view(template_name='cards.html'), name='cards'),
    path('charts/', TemplateView.as_view(template_name='charts.html'), name='charts'),
    path('forgot-password/', TemplateView.as_view(template_name='forgot-password.html'), name='forgot-password'),
    path('login/', TemplateView.as_view(template_name='login.html'), name='login'),
    path('register/', TemplateView.as_view(template_name='register.html'), name='register'),
    path('tables/', TemplateView.as_view(template_name='tables.html'), name='tables.html'),
    path('utilities-animation/', TemplateView.as_view(template_name='utilities-animation.html'), name='utilities-animation'),
    path('utilities-border/', TemplateView.as_view(template_name='utilities-border.html'),
         name='utilities-border'),
    path('utilities-color/', TemplateView.as_view(template_name='utilities-color.html'),
         name='utilities-color'),
    path('utilities-other/', TemplateView.as_view(template_name='utilities-other.html'),
         name='utilities-other'),
]
