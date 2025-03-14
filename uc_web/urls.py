"""
URL configuration for uc_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from uc_web import pages, api

urlpatterns = [
    path('', pages.main),

    path('add-post', pages.add_post),
    path('posts/<int:id>', pages.post_detail),

    path('sign-in', pages.sign_in),
    path('register', pages.register),

    path('api/auth/sign-in', api.sign_in),
    path('api/auth/register', api.register),
    path('api/auth/csrf-token', api.csrf_token),

    path('api/posts', api.posts),

    path('admin/', admin.site.urls),
]
