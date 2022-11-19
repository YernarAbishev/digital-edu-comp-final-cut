from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
import random


# басты бет
def mainPage(request):
    return render(request, "pages/home.html")

# жоба туралы
def aboutProjectPage(request):
    return render(request, "pages/about.html")

# курстар
def courseList(request, slug=None):
    category = None
    categories = Category.objects.all()
    searchCourse = request.GET.get('search')

    if searchCourse:
        courses = Course.objects.filter(Q(courseName__icontains=searchCourse) or Q(courseDescription__icontains=searchCourse))
    else:
        courses = Course.objects.all().order_by('-postDate')
    if slug:
        category = get_object_or_404(Category, slug=slug)
        courses = courses.filter(category=category)
    return render(request, "pages/course-list.html", {
        'category': category,
        'categories': categories,
        'courses': courses
    })

# плейлист
def playList(request, slug=None):
    course = None
    courses = Course.objects.all()
    themes = Theme.objects.all()
    if slug:
        course = get_object_or_404(Course, slug=slug)
        themes = themes.filter(course=course)
    return render(request, "pages/playlist.html", {
        'course': course,
        'courses': courses,
        'themes': themes,
    })

# сабақ
@login_required
def themeDetail(request, slug, pk):
    color = "%06x" % random.randint(0, 0xFFFFFF)
    course = get_object_or_404(Course, slug=slug)
    theme = get_object_or_404(Theme, pk=pk)
    themes = Theme.objects.all()
    comments = theme.comments.filter(active=True).order_by('-created_on')
    newComment = None
    if request.method == "POST":
        form = CommentForm(data=request.POST)
        if form.is_valid():
            newComment = form.save(commit=False)
            newComment.theme = theme
            newComment.user = request.user;
            newComment.save()
    else:
        form = CommentForm()

    if slug:
        themes = themes.filter(course=course)
    return render(request, "pages/lesson-detail.html", {
        'course': course,
        'theme': theme,
        'themes': themes,
        'comments': comments,
        'newComment': newComment,
        'form': form,
        'color': color
    })



def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Тіркелу сәтті аяқталды.")
            return redirect("mainPage")
        messages.error(request, "Тіркелу барысында қателер кетті. Қайтадан көріңіз.")
    else:
        form = NewUserForm()
    return render(request, "user/sign-up.html", {
        'form': form
    })

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Қош келдіңіз, {username}.")
                return redirect("mainPage")
            else:
                messages.error(request, "Логин немесе пароль қате")
        else:
            messages.error(request, "Логин немесе пароль қате")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "Сіз платформадан шықтыңыз.")
    return redirect("mainPage")