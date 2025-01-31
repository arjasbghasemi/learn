from main.models import Category, SubCategory, Lesson,Menu,SubSubCategory,SubSubSubCategory


def context_processor(request):
    cats_proc=Category.objects.all()
    sub_cats_proc=SubCategory.objects.all()
    sub_sub_cats_proc=SubSubCategory.objects.all()
    sub_sub_sub_cats_proc=SubSubSubCategory.objects.all()
    lessons_proc=Lesson.objects.all()
    menus=Menu.objects.all()
    cat_pks=lessons_proc.values_list('category__pk',flat=True)
    menu_pks=lessons_proc.values_list('menu__pk',flat=True)
    sub_cat_pks=lessons_proc.values_list('subcategory__pk', flat=True)
    lessons_proc_men=Lesson.objects.filter(menu=None)
    lessons_proc_cats=Lesson.objects.filter(category=None)
    return {'sub_sub_cats_proc':sub_sub_cats_proc,'cats_proc':cats_proc,'sub_cats_proc':sub_cats_proc,'lessons_proc_cats':lessons_proc_cats,'sub_sub_sub_cats_proc':sub_sub_sub_cats_proc,'lessons_proc':lessons_proc,'lessons_proc_men':lessons_proc_men,'sub_cat_pks':sub_cat_pks,'menus':menus,'cat_pks':cat_pks,'menu_pks':menu_pks}