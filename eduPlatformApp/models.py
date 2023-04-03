from django.db import models
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import Q
from tinymce.models import HTMLField


class Category(models.Model):
    categoryName = models.CharField("Category name", max_length=255)
    slug = models.SlugField("URL category", unique=True)

    def __str__(self):
        return self.categoryName

    def get_absolute_url(self):
        return reverse("courseListByCategory", args=[self.slug])

    class Meta:
        verbose_name_plural = "Categories"

class Course(models.Model):
    courseName = models.CharField("Course name", max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")
    courseDescription = models.TextField("Course description")
    courseCover = models.ImageField("Course cover")
    postDate = models.DateTimeField(default=datetime.now)
    slug = models.SlugField("URL course", unique=True)

    def get_absolute_url(self):
        return reverse("playList", args=[self.slug])

    def __str__(self):
        return self.courseName

    class Meta:
        verbose_name_plural = "Courses"


class Theme(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    themeName = models.CharField("Theme name", max_length=255)
    themeDescription = HTMLField("Theme Description")
    videoUrl = models.CharField("Video URL", max_length=500)

    def __str__(self):
        return self.themeName

    def get_absolute_url(self):
        return reverse("themeDetail", args=[self.pk])

    class Meta:
        verbose_name_plural = "Themes"

class Comment(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User,
                        default = 1,
                        null = True, 
                        on_delete = models.SET_NULL
                        )
    body = models.TextField("Пікір қалдыру")
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Пікір: {} - {}'.format(self.body, self.user)