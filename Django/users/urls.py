# users/urls.py

from django.urls import path

from . import views

#from users.views import SignUp

from users.views import register,logout


urlpatterns = [
    #path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/', register, name='signup'),  # <-- added
    path('logout/', logout, name='logout'), # <-- added logout
]