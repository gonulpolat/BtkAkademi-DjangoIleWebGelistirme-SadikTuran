from django.contrib import admin

from .models import Category, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'isActive', 'isHome', 'category_list')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',),}
    list_filter = ('isActive', 'isHome')
    list_editable = ('isActive', 'isHome')
    search_fields = ('title', 'description')


    def category_list(self, obj):
        text = ""
        for category in obj.categories.all():
            text += category.name + " / "
        return text


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'course_count',)
    prepopulated_fields = {'slug': ('name',),}


    def course_count(self, obj):
        return obj.course_set.count()