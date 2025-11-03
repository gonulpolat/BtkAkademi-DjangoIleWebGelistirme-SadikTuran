from django.contrib import admin

from .models import Category, Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'isActive')
    list_display_links = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',),}    # model üzerindeki save() methodunu kaldırdın. Add Course sayfasında slug alanı görünüyor, sen title bilgisini oluşturdukça bu alan da otomatik yazılıyor, farkı ise artık slug alanını sen de değiştirebilirsin
    list_filter = ('isActive', 'category')
    list_editable = ('isActive',) # Change course sayfasına gitmeden isActive alanı değiştirilebilir
    search_fields = ('title', 'description')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
