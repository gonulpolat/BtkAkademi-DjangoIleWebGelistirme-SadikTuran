from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def courses(request):
    return HttpResponse("Kurs Listesi")

def details(request):
    return HttpResponse("Kurs Detay Sayfası")

def programming(request):
    return HttpResponse("Programlama Kurs Listesi")

def mobile_apps(request):
    return HttpResponse("Mobil Uygulamalar")

def get_courses_by_category(request, category):
    return HttpResponse(f"{category} Kategorisine Göre Kurs Listesi")