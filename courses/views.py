from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
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

def details(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
    except:
        raise Http404()
    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def programming(request):
    return HttpResponse("Programlama Kurs Listesi")

def mobile_apps(request):
    return HttpResponse("Mobil Uygulamalar")

def get_courses_by_category_name(request, category_name):
    try:
        category_text = data[category_name]
        return render(request, 'courses/courses.html', {
            'category': category_name,
            'category_text': category_text,
        })
    except:
        return HttpResponseNotFound("<h1>Yanlış Kategori Seçimi</h1>")
        

def get_courses_by_category_id(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori Seçimi")
    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category_name", args=[category_name])  # url içerisinde birden fazla dinamik bölüm olabilir, bu nedenle args parametresi liste ile gönderilir

    return redirect(redirect_url)
    