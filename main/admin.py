from django.contrib import admin
from .models import *


# Register your models here.
class AdminSubCategory(admin.ModelAdmin):
    list_display = ['title','menu', 'category']
    list_display_links = ['title']
    list_editable = ['menu', 'category']
class AdminLink(admin.StackedInline):
    model=Link
    extra=0
class AdminLesson(admin.ModelAdmin):
    list_display = ['title','menu','category','subcategory','subsubcategory']
    list_display_links = ['title']
    list_editable = ['menu','category','subcategory','subsubcategory']
    inlines = [AdminLink]

class AdminCategory(admin.ModelAdmin):
    list_display = ['title', 'menu']
    list_display_links = ['title']
    list_editable = ['menu']

class AdminSubSubCategory(admin.ModelAdmin):
    list_display = ['title', 'menu', 'category', 'subcategory']
    list_display_links = ['title']
    list_editable = ['menu', 'category', 'subcategory']

class AdminSubSubSubCategory(admin.ModelAdmin):
    list_display = ['title', 'menu', 'category', 'subcategory','subsubcategory']
    list_display_links = ['title']
    list_editable = ['menu', 'category', 'subcategory','subsubcategory']

admin.site.register(Menu)
admin.site.register(Category,AdminCategory)
admin.site.register(SubCategory, AdminSubCategory)
admin.site.register(SubSubCategory, AdminSubSubCategory)
admin.site.register(SubSubSubCategory, AdminSubSubSubCategory)
admin.site.register(Lesson,AdminLesson)
# admin.site.register(UserLessons)
admin.site.register(Comment)

