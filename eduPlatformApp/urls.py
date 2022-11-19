from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('about/', views.aboutProjectPage, name='aboutProjectPage'),
    path('courses/', views.courseList, name='courseList'),
    path('courses/<slug:slug>/', views.courseList, name='courseListByCategory'),
    path('courses/<slug:slug>/lessons/', views.playList, name='playList'),
    path('courses/<slug:slug>/lessons/<int:pk>/', views.themeDetail, name='themeDetail'),
    path('sign-up/', views.signUp, name='signUp'),
    path('login/', views.logIn, name='logIn'),
    path('logout/', views.logoutUser, name='logoutUser'),
]