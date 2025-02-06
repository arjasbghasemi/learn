from django.contrib import admin
from .models import *


# Register your models here.
class AdminSubCategory(admin.ModelAdmin):
    list_display = ['title','menu', 'category']
    list_display_links = ['title']
    list_editable = ['menu', 'category']
    search_fields = ['title','menu__title','category__title']
class AdminLink(admin.StackedInline):
    model=Link
    extra=0
class AdminLesson(admin.ModelAdmin):
    list_display = ['title','menu','category','subcategory','subsubcategory']
    list_display_links = ['title']
    list_editable = ['menu','category','subcategory','subsubcategory']
    search_fields = ['title', 'menu__title', 'category__title','subcategory__title','subsubcategory__title','subsubsubcategory__title','text','date','link__url','link__title']
    inlines = [AdminLink]

class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'menu']
    list_display_links = ['title']
    list_editable = ['menu']
    search_fields = ['title','menu__title']

class AdminSubSubCategory(admin.ModelAdmin):
    list_display = ['title', 'menu', 'category', 'subcategory']
    list_display_links = ['title']
    list_editable = ['menu', 'category', 'subcategory']
    search_fields = ['title', 'menu__title','subcategory__title','category__title']
class AdminSubSubSubCategory(admin.ModelAdmin):
    list_display = ['title', 'menu', 'category', 'subcategory','subsubcategory']
    list_display_links = ['title']
    list_editable = ['menu', 'category', 'subcategory','subsubcategory']
    search_fields = ['title', 'menu__title', 'category__title','subcategory__title','subsubcategory__title']
class AdminMenu(admin.ModelAdmin):
    search_fields = ['title']
admin.site.register(Menu,AdminMenu)
admin.site.register(Category,AdminCategory)
admin.site.register(SubCategory, AdminSubCategory)
admin.site.register(SubSubCategory, AdminSubSubCategory)
admin.site.register(SubSubSubCategory, AdminSubSubSubCategory)
admin.site.register(Lesson,AdminLesson)
admin.site.register(Comment)

