from django.shortcuts import render, redirect
from django.http import FileResponse
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    lessons = Lesson.objects.filter(main_page=True)
    lessons_new = Lesson.objects.order_by('-date').filter(main_page=True)
    if len(lessons_new) > 5:
        lessons_new = lessons_new[:5]
    return render(request, 'main/index.html', {'lessons': lessons,'lessons_new':lessons_new})

def lesson(request, pk):
    if not request.user.is_authenticated:
        return redirect('signin')
    lesson = Lesson.objects.get(pk=pk)
    lessons= Lesson.objects.order_by('-date').filter(main_page=True)
    lesson_links=Link.objects.filter(lesson=lesson)
    # lesson_user,_=UserLessons.objects.get_or_create(user=request.user)
    # list_value=[i[0] for i in  lesson_user.lessons.all().values_list('value')]
    # if lesson not in lesson_user.lessons.all():
    #     if lesson.value==0 or lesson.value - 1 in list_value:
    #         lesson_user.lessons.add(lesson)
    #         lesson_user.save()
    #     else:
    #         messages.warning(request,'لطفا درس قبلی را مشاهده کنید!')
    #         return redirect('index')
    if len(lessons)>5:
        lessons= lessons[:5]
    return render(request, 'main/lesson.html', {'lesson': lesson,'lessons':lessons,'lesson_links':lesson_links})


def lesson_menu(request, pk_menu):
    lesson = Lesson.objects.get(menu__pk=pk_menu, category=None, subcategory=None, subsubcategory=None)
    lessons = Lesson.objects.order_by('-date').filter(main_page=True)
    if len(lessons) > 5:
        lessons = lessons[:5]
    return render(request, 'main/lesson.html', {'lesson': lesson,'lessons':lessons})


def lesson_cat(request, pk_menu, pk_cat):
    lesson = Lesson.objects.get(menu__pk=pk_menu, category__pk=pk_cat, subcategory=None, subsubcategory=None)
    lessons = Lesson.objects.order_by('-date').filter(main_page=True)
    if len(lessons) > 5:
        lessons = lessons[:5]
    return render(request, 'main/lesson.html', {'lesson': lesson,'lessons':lessons})


def lesson_sub_cat(request, pk_menu, pk_cat, pk_sub_cat):
    lesson = Lesson.objects.get(menu__pk=pk_menu, category=pk_cat, subcategory=pk_sub_cat, subsubcategory=None)
    lessons = Lesson.objects.order_by('-date').filter(main_page=True)
    if len(lessons) > 5:
        lessons = lessons[:5]
    return render(request, 'main/lesson.html', {'lesson': lesson,'lessons':lessons})


def lesson_sub_sub_cat(request, pk_menu, pk_cat, pk_sub_cat, pk_sub_sub_cat):
    lesson = Lesson.objects.get(menu__pk=pk_menu, category__pk=pk_cat, subcategory__pk=pk_sub_cat,
                                subsubcategory__pk=pk_sub_sub_cat)
    lessons = Lesson.objects.order_by('-date').filter(main_page=True)
    if len(lessons) > 5:
        lessons = lessons[:5]
    return render(request, 'main/lesson.html', {'lesson': lesson,'lessons':lessons})
def lesson_sub_sub_sub_cat(request, pk_menu, pk_cat, pk_sub_cat, pk_sub_sub_cat,pk_sub_sub_sub_cat):
    lesson = Lesson.objects.get(menu__pk=pk_menu, category__pk=pk_cat, subcategory__pk=pk_sub_cat,
                                subsubcategory__pk=pk_sub_sub_cat,subsubsubcategory__pk=pk_sub_sub_sub_cat)
    lessons = Lesson.objects.order_by('-date').filter(main_page=True)
    if len(lessons) > 5:
        lessons = lessons[:5]
    return render(request, 'main/lesson.html', {'lesson': lesson,'lessons':lessons})

def search(request):
    if request.method=='POST':
        search=request.POST['search']
        lessons = Lesson.objects.filter(text__icontains=search,main_page=True)
        lessons_new = Lesson.objects.order_by('-date').filter(main_page=True)
        if len(lessons_new) > 5:
            lessons_new = lessons_new[:5]
        return render(request, 'main/index.html', {'lessons': lessons,'lessons_new':lessons_new})

def download_file(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    return FileResponse(lesson.pdf)