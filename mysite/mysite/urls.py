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
    path('buttons.html', TemplateView.as_view(template_name='buttons.html'), name='buttons.html'),
    path('cards.html', TemplateView.as_view(template_name='cards.html'), name='cards.html'),
    path('charts.html', TemplateView.as_view(template_name='charts.html'), name='charts.html'),
    path('forgot-password.html', TemplateView.as_view(template_name='forgot-password.html'), name='forgot-password.html'),
    path('login.html', TemplateView.as_view(template_name='login.html'), name='login.html'),
    path('register.html', TemplateView.as_view(template_name='register.html'), name='register.html'),
    path('tables.html', TemplateView.as_view(template_name='tables.html'), name='tables.html'),
    path('utilities-animation.html', TemplateView.as_view(template_name='utilities-animation.html'), name='utilities-animation.html'),
    path('utilities-border.html', TemplateView.as_view(template_name='utilities-border.html'),
         name='utilities-border.html'),
    path('utilities-color.html', TemplateView.as_view(template_name='utilities-color.html'),
         name='utilities-color.html'),
    path('utilities-other.html', TemplateView.as_view(template_name='utilities-other.html'),
         name='utilities-other.html'),
]