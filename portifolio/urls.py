from django.urls import path
from . import views
from .views import contact_view

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects, name='projects'),
    path('contact/', contact_view, name='contact'),
    path('certifications/', views.certifications, name='certifications'),
     path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
     
]
