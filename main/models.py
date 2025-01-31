from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
# Create your models here.
class Menu(models.Model):
    title=models.CharField(max_length=100)
    has_tree=models.BooleanField(default=False)
    def __str__(self):
        return self.title
class Category(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    has_tree=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    has_tree=models.BooleanField(default=False)

    def __str__(self):
        return self.title

class SubSubCategory(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    has_tree=models.BooleanField(default=False)
    def __str__(self):
        return self.title
class SubSubSubCategory(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True,null=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Lesson(models.Model):
    menu=models.ForeignKey(Menu,on_delete=models.CASCADE,blank=True,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True,null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,blank=True,null=True)
    subsubcategory = models.ForeignKey(SubSubCategory, on_delete=models.CASCADE,blank=True,null=True)
    subsubsubcategory = models.ForeignKey(SubSubSubCategory, on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="lessons/image/",blank=True,null=True)
    video = models.FileField(upload_to="lessons/video/",blank=True,null=True)
    voice = models.FileField(upload_to="lessons/voice/",blank=True,null=True)
    text = models.TextField(blank=True,null=True)
    views = models.IntegerField(default=0)
    date = models.DateField(default=datetime.now)
    value=models.IntegerField(default=0,unique=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    text=models.TextField(blank=True,null=True)
    date=models.DateField(default=datetime.now)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.title



class UserLessons(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    lessons=models.ManyToManyField(Lesson,blank=True,null=True)
    def __str__(self):
        return str(self.user)


