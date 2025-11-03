from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Category, Course

data = {
    "programlama": "Programlama Kategorisine Ait Kurslar",
    "web-gelistirme": "Web Geliştirme Kategorisine Ait Kurslar",
    "mobil-uygulamalar": "Mobil Uygulamalar Kategorisine Ait Kurslar",
}

def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'courses': kurslar,
        'categories': kategoriler,
    })

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def programming(request):
    return HttpResponse("Programlama Kurs Listesi")

def mobile_apps(request):
    return HttpResponse("Mobil Uygulamalar")

def get_courses_by_category(request, slug):
    kurslar = Course.objects.filter(category__slug = slug, isActive = 1)
    kategoriler = Category.objects.all()

    context = {
        'courses': kurslar,
        'categories': kategoriler,
        'selected_category': slug,
    }

    return render(request, 'courses/index.html', context)
    