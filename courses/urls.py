from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.search),
    path('<slug:slug>/', views.details, name="course_details"),
    path('kategori/<slug:slug>/', views.get_courses_by_category, name="courses_by_category"),
]
