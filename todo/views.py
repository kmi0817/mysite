from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import *
from .forms import homeworkForm
from .filters import CourseFilter

def index(request) :
    course_list = Course.objects.all()

    myFilter = CourseFilter(request.GET, queryset=course_list)
    course_list = myFilter.qs

    context = {'course_list' : course_list, 'myFilter' : myFilter}
    return render(request, 'todo/index.html', context)

def detail(request, homework_id) :
    hw = get_object_or_404(Homework, pk=homework_id)
    context = {'hw' : hw}
    return render(request, 'todo/detail.html', context)

def createForm(request) :
    form = homeworkForm()

    if request.method == 'POST' :
        form = homeworkForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect(reverse('todo:index'))
    
    context = {'form' : form}
    return render(request, 'todo/form.html', context)

def updateForm(request, homework_id) :
    homework = get_object_or_404(Homework, pk=homework_id)
    form = homeworkForm(instance=homework)

    if request.method == 'POST' :
        form = homeworkForm(request.POST, instance=homework)
        if form.is_valid() :
            form.save()
            return redirect(reverse('todo:index'))

    context = {'form' : form}
    return render(request, 'todo/form.html', context)

def deleteForm(request, homework_id) :
    homework = get_object_or_404(Homework, pk=homework_id)
    homework.delete()
    return redirect(reverse('todo:index'))