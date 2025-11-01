from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

data = {
    "programlama": "Programlama Kategorisine Ait Kurslar",
    "web-gelistirme": "Web Geliştirme Kategorisine Ait Kurslar",
    "mobil-uygulamalar": "Mobil Uygulamalar Kategorisine Ait Kurslar",
}

def index(request):
    return render(request, 'courses/index.html')

def courses(request):
    category_list = list(data.keys())
    list_items = ""
    for category in category_list:
        redirect_url = reverse('courses_by_category_name', args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>Kurs Listesi</h1><br><ul>{list_items}</ul>"

    return HttpResponse(html)

def details(request, course_name):
    return HttpResponse(f"{course_name} Detay Sayfası")

def programming(request):
    return HttpResponse("Programlama Kurs Listesi")

def mobile_apps(request):
    return HttpResponse("Mobil Uygulamalar")

def get_courses_by_category_name(request, category_name):
    try:
        category_text = data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("<h1>Yanlış Kategori Seçimi</h1>")
        

def get_courses_by_category_id(request, category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori Seçimi")
    category_name = category_list[category_id - 1]

    redirect_url = reverse("courses_by_category_name", args=[category_name])  # url içerisinde birden fazla dinamik bölüm olabilir, bu nedenle args parametresi liste ile gönderilir

    return redirect(redirect_url)
    