"""config URL Configuration

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
from django.urls import path, include #new
from django.views.generic.base import TemplateView # new
from . import views #new 20200602
from users import views # from users app import views file
from users.views import home, pricing, about, register, logout, get_ContactForm
from config.views import feature # import feature from views
import users.urls
from config.views import Comment, Chart, Renew

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), #new => refer to 1.1
    path('', home),
    path('pricing/',pricing), #new
    path('accounts/', include('users.urls')), # new 20200603 for users signup # for user signout
    path('about/', about),
    path('feature/', feature),
    path('Comment/', get_ContactForm),
    path('Chart/', Chart),
    path('Renew/', Renew),
]

#1.1
# for structure under django.contrib.auth.urls
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']
