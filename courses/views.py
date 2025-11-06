from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Category, Course, UploadModel


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

# http://127.0.0.1:8000/accounts/login/?next=/kurs/create-course -> login olmayan kullanıcı Kurs Ekle sayfasına gitmeye çalışırsa bu sayfaya yönlendirilir
@login_required(login_url='/account/login')   # şimdi bu sayfaya yönlenir
def create_course(request):
    if request.method == 'POST':
        form = CourseCreateForm(request.POST, request.FILES)
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
        form = CourseEditForm(request.POST, request.FILES, instance=course)
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
        form = UploadForm(request.POST, request.FILES) # Text bilgileri request.POST ögesinden; files bilgileri request.FILES ögesinden gelir
        if form.is_valid():
            model = UploadModel(image=request.FILES['image'])
            model.save()
            return render(request, 'courses/success.html')
    else:
        form = UploadForm()
    return render(request, 'courses/upload.html', {'form': form})

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
    