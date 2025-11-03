from django.contrib import admin

from .models import Category, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'isActive')
    list_display_links = ('title', 'slug')
    readonly_fields = ('slug',)  # slug alanı editable olmadığı için Change course sayfasında da görünmüyordu, artık görünür
    list_filter = ('isActive',)
    list_editable = ('isActive',) # Change course sayfasına gitmeden isActive alanı değiştirilebilir
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
