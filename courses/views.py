from datetime import date, datetime
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Course

data = {
    "programlama": "Programlama Kategorisine Ait Kurslar",
    "web-gelistirme": "Web Geliştirme Kategorisine Ait Kurslar",
    "mobil-uygulamalar": "Mobil Uygulamalar Kategorisine Ait Kurslar",
}

db = {
    "courses": [
        {
            "title": "JavaScript Kursu",
            "description": "JavaScript, HTML ve CSS ile birlikte World Wide Web'in temel teknolojilerinden biri olan programlama dilidir. Web sitelerinin %97'sinden fazlası, web sayfası hareketleri için istemci tarafında JavaScript kullanırlar ve kullanılan kodlar genellikle üçüncü taraf kitaplıkları içerir.",
            "imageUrl": "javascript.webp",
            "slug": "javascript-kursu",
            "date": datetime.now(),
            "isActive": True,
            "isUpdated": True,
        },
        {
            "title": "Python Kursu",
            "description": "Python, nesne yönelimli, yorumlamalı, birimsel ve etkileşimli yüksek seviyeli bir programlama dilidir. Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır.",
            "imageUrl": "python.webp",
            "slug": "python-kursu",
            "date": date(2025,11,12),
            "isActive": False,
            "isUpdated": True,
        },
        {
            "title": "Web Geliştirme Kursu",
            "description": "Web development, internet üzerinden erişilebilen web siteleri ve web tabanlı uygulamaların oluşturulması sürecidir.",
            "imageUrl": "web-gelistirme.webp",
            "slug": "web-gelistirme-kursu",
            "date": date(2025,10,23),
            "isActive": True,
            "isUpdated": False,
        },
    ],
    "categories": [
        {
            "id": 1,
            "name": "programlama",
            "slug": "programlama",
        },
        {
            "id": 2,
            "name": "web geliştirme",
            "slug": "web-gelistirme",
        },
        {
            "id": 3,
            "name": "mobil uygulamalar",
            "slug": "mobil-uygulamalar",
        },
    ]
}

def index(request):
    kurslar = Course.objects.filter(isActive=1)
    kategoriler = db['categories']

    return render(request, 'courses/index.html', {
        'courses': kurslar,
        'categories': kategoriler,
    })

def details(request, course_name):
    return HttpResponse(f"{course_name} Detay Sayfası")

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
    