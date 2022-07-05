from django import forms
from .models import *


class AddPostForm(forms):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    class Meta:
        model = News
        fields = '__all__'


class AddPosterForm(forms):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    class Meta:
        model = Poster
        fields = ['title', 'date_provide', 'text_short', 'text', 'photo']


class AddTeacherForm(forms):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    class Meta:
        model = Teacher
        fields = ['name', 'info', 'photo', 'subject']


class AddAwardForm(forms):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    class Meta:
        model = Award
        fields = ['owner', 'describe', 'photo']


class AddWorkForm(forms):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    class Meta:
        model = Work
        fields = ['name', 'author', 'photo']


class AddDocsForm(forms):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    class Meta:
        model = Docs
        fields = ['studyProgram', 'timetable',
                  'graduates', 'pupil', 'departments',
                  'charter', 'inn',
                  'classrooms', 'datetime']


class AddLicenseForm(forms):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)

    class Meta:
        model = License
        fields = ['license']
