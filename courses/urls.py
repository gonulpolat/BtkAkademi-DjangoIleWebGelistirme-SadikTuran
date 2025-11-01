from django.http import HttpResponse
from django.urls import path

def home(request):
    return HttpResponse("Anasayfa")

def courses(request):
    return HttpResponse("Kurs Listesi")

urlpatterns = [
    path('', home),
    path('anasayfa', home),
    path('kurslar', courses),
]
