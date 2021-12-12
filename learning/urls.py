from django.urls import path, include
from . import views


urlpatterns = [
    # Shared Paths
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.LoginView.as_view(), name='login'),
    # path('logout/', views.logoutView, name='logout'),
]
