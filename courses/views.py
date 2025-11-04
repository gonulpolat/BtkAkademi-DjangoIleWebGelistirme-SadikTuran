from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import Category, Course


def index(request):
    kurslar = Course.objects.filter(isActive=1, isHome=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'courses': kurslar,
        'categories': kategoriler,
    })

def search(request):
    if 'q' in request.GET and request.GET['q'] != '':
        q = request.GET['q']
        kurslar = Course.objects.filter(isActive = 1, title__contains=q).order_by('date')
        kategoriler = Category.objects.all()
    else:
        return redirect('/kurs')

    context = {
        'courses': kurslar,
        'categories': kategoriler,
    }

    return render(request, 'courses/search.html', context)

def details(request, slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def get_courses_by_category(request, slug):
    kurslar = Course.objects.filter(categories__slug = slug, isActive = 1).order_by('date')
    kategoriler = Category.objects.all()

    paginator = Paginator(kurslar, 2)
    page = request.GET.get('page', 1)   
    page_obj = paginator.page(page) # page fonksiyonu ya da get_page fonksiyonunu kullanabilirsin

    context = {
        'page_obj': page_obj,
        'categories': kategoriler,
        'selected_category': slug,
    }

    return render(request, 'courses/list.html', context)
    