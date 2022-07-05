from django.shortcuts import render, get_object_or_404
import os
"""from django.views import reverse_lazy"""
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

# Create your views here.


class NewsHome(ListView):
    model = News
    template_name = 'main/NewsList.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Новости'
        return context

    def get_queryset(self):
        return News.objects.all().order_by('date')


class AwardHome(ListView):
    model = Award
    template_name = 'main/list_award.html'
    context_object_name = 'awards'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Награды'
        return context

    def get_queryset(self):
        return Award.objects.all().order_by('date')


class PostersHome(ListView):
    model = Poster
    template_name = 'main/list_poster.html'
    context_object_name = 'poster'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        scans = Poster.objects.all().order_by('date_provide')
        context['title'] = 'Афишы'
        return context

    def get_queryset(self):
        return Poster.objects.all().order_by('date_provide')


class TeachersHome(ListView):
    model = Teacher
    template_name = 'main/list_teacher.html'
    context_object_name = 'teacher'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(** kwargs)
        context['title'] = 'Учителя'
        return context

    def get_queryset(self):
        return Teacher.objects.all()


def main(request):
    news = News.objects.all()
    works = Work.objects.all().order_by('-date')
    works = works[0:8]
    scans = Poster.objects.all().order_by('date_provide')
    if len(scans) > 2:
        post1 = scans[0]
        post2 = scans[1]
        post3 = scans[2]
    else:
        post1 = None
        post2 = None
        post3 = None
    context = {
        'works': works,
        'title': 'Главная',
        'news': news,
        'poster1': post1,
        'poster2': post2,
        'poster3': post3,

    }
    return render(request, 'main/index.html', context=context)


def students(request):
    context = {
        'title': 'Ученику'
    }
    return render(request, 'main/for_students.html', context=context)


def applicants(request):
    context = {
        'title': 'Поступающему'
    }
    return render(request, 'main/for_applicants.html', context=context)


def about(request):
    context = {
        'title': 'О школе'
    }
    return render(request, 'main/about_school.html', context=context)


def show_news(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {
        'content': news,
        'title': news.title,
    }
    return render(request, 'main/universal.html', context=context)


def show_poster(request, poster_id):
    poster = get_object_or_404(Poster, pk=poster_id)
    context = {
        'content': poster,
        'title': poster.title,
    }
    return render(request, 'main/universal.html', context=context)


def show_teacher(request, teacher_id):
    teacher = get_object_or_404(Poster, pk=teacher_id)
    context = {
        'content': teacher,
        'title': 'Учителя',
    }
    return render(request, 'main/universal.html', context=context)


def show_work(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    context = {
        'content': work,
        'title': 'Работа',
    }
    return render(request, 'main/universal.html', context=context)


def delete_poster(request, poster_id):
    poster = Poster.objects.get(pk=poster_id)
    poster.delete()


def show_award(request, award_id):
    award = get_object_or_404(Award, pk=award_id)
    context = {
        'content': award,
        'title': 'Награда'
    }
    return render(request, 'main/universal.html', context=context)


def show_inn(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.inn,
        'title': 'Document'
    }
    return render(request, 'main/inn.html', context=context)


def show_study_program(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.studyProgram,
        'title': 'Document'
    }
    return render(request, 'main/doc_view.html', context=context)


def show_timetable(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.timetable,
        'title': 'Document'
    }
    return render(request, 'main/doc_view.html', context=context)


def show_graduates(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.graduates,
        'title': 'Document'
    }
    return render(request, 'main/doc_view.html', context=context)


def show_departments(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.departments,
        'title': 'Document'
    }
    return render(request, 'main/doc_view.html', context=context)


def show_charter(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.charter,
        'title': 'Document'
    }
    return render(request, 'main/charter_view.html', context=context)


def show_classrooms(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.classrooms,
        'title': 'Document'
    }
    return render(request, 'main/doc_view.html', context=context)


def show_students(request):
    doc = Docs.objects.last()
    context = {
        'doc': doc.students,
        'title': 'Document'
    }
    return render(request, 'main/doc_view.html', context=context)


def show_license(request):
    lic = License.objects.all().order_by('-datetime')
    context = {
        'lic': lic,
        'title': 'Лицензии'
    }
    return render(request, 'main/lis_view.html', context=context)

'''class RegisterUser(DataMixin, CreateView):
    form_class = UserCreatingForm
    template_name = 'main/reg.html'
    success_url = reverse_lazy('main/log.html')'''
