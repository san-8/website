from django.urls import path
from .views import Userdetail, Userlist, AppCreate, AppUpdate, AppDelete, ClerkLogin, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',ClerkLogin.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('register/',Register.as_view(),name="register"),
    path('',Userlist.as_view(),name='users'),
    path('users/<int:pk>/',Userdetail.as_view(),name='user'),
    path('create-app/',AppCreate.as_view(),name='create-app'),
    path('app-edit/<int:pk>/',AppUpdate.as_view(),name='app-edit'),
    path('app-delete/<int:pk>/',AppDelete.as_view(),name='app-delete'),
]