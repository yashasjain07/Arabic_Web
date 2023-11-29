"""
URL configuration for online_teach project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from Arabic import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Phase1/', views.phase1, name = 'phase1'),
    path('Phase1/easy/', views.easy, name = 'easy'),
    path('Phase1/easyquiz/', views.easyquiz, name = 'easyquiz'),
    path('Phase1/medium/', views.medium, name = 'medium'),
    path('Phase1/mediumquiz/', views.mediumquiz, name = 'mediumquiz'),
    path('Phase1/hard/', views.hard, name = 'hard'),
    path('Phase1/hardquiz/', views.hardquiz, name = 'hardquiz'),
    path('Phase2/', views.phase2, name = 'phase2'),
    path('Phase2/easy/', views.P2easy, name = 'P2easy'),
    path('Phase2/easyquiz/', views.P2easyquiz, name = 'P2easyquiz'),
    path('Phase2/medium/', views.P2medium, name = 'P2medium'),
    path('Phase2/mediumquiz/', views.P2mediumquiz, name = 'P2mediumquiz'),
    path('Phase2/hard/', views.P2hard, name = 'P2hard'),
    path('Phase2/hardquiz/', views.P2hardquiz, name = 'P2hardquiz'),
]
