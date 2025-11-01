from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses),
    path('liste', views.courses),
    path('detay', views.details),
    path('programlama', views.programming),
    path('mobil-uygulamalar', views.mobile_apps),
]
