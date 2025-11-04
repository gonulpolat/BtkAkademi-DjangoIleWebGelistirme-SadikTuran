from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Category, Course


def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = Category.objects.all()

    return render(request, 'courses/index.html', {
        'courses': kurslar,
        'categories': kategoriler,
    })

def search(request):
    print(request.GET)   
    # http://127.0.0.1:8000/kurs/search?q=python               -> <QueryDict: {'q': ['python']}>
    # http://127.0.0.1:8000/kurs/search?q=python&order_by=date -> <QueryDict: {'q': ['python'], 'order_by': ['date']}>

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

    return render(request, 'courses/index.html', context)
    