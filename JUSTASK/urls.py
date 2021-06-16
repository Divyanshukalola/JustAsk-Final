"""JUSTASK URL Configuration

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
from django.urls import path, include
from main import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf.urls.static import static  

urlpatterns = [
	path('', include('main.urls')),
    path('justask04081999-admin/', admin.site.urls),
    path('justask-admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),


    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset.html',html_email_template_name='registration/password_reset_e.html',subject_template_name='registration/password_reset_s.txt'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_d.html'
         ),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_c.html'
         ),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_comp.html'
         ),
         name='password_reset_complete'),


   
    
]



admin.site.site_header = "Just Ask Admin"
admin.site.site_title = "Just Ask Admin Portal"
admin.site.index_title = "Welcome to Just Ask Portal"

