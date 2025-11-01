from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('liste/', views.courses),
    path('<course_name>/', views.details),
    path('kategori/<int:category_id>/', views.get_courses_by_category_id),
    path('kategori/<str:category_name>/', views.get_courses_by_category_name, name="courses_by_category_name"),
]
