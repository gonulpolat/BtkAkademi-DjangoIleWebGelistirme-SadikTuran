from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseCreateForm, CourseEditForm
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

def create_course(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST)
        if form.is_valid():
            # verileri tek tek yazmana gerek yok zaten model üzerinden geliyor
            form.save()
            return redirect('/kurs')
    else:
        form = CourseCreateForm()

    context = {
        'form': form,
    }

    return render(request, 'courses/course-create.html', context)

def course_list(request):
    kurslar = Course.objects.all()
    return render(request, 'courses/course-list.html', {
        'courses': kurslar,
    })

def course_edit(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        form = CourseEditForm(request.POST, instance=course)
        form.save()
        return redirect('course_list')
    else:
        form = CourseEditForm(instance=course)
    return render(request, 'courses/course-edit.html', {'form': form,})

def course_delete(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'courses/course-delete.html', {'course':course})

def upload(request):
    if request.method == 'POST':
        uploaded_image =  request.FILES['image']
        handle_uploaded_files(uploaded_image)
        return render(request, 'courses/success.html')
    return render(request, 'courses/upload.html')

def handle_uploaded_files(file):
    with open('temp/' + file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

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
    