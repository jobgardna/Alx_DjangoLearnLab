from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
#from .views import list_books, LibraryDetailView, register, homepage

urlpatterns = [
    path('', views.homepage, name='home'),
    path('books/', views.list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Auth URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]