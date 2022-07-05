from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from .views import *


urlpatterns = [
    path('', main, name='home'),
    path('students/', students, name='children'),
    path('about/', about, name='about'),
    path('applicants/', applicants, name='abiturient'),
    path('posters/', PostersHome.as_view(), name='poster-list'),
    path('teachers/', TeachersHome.as_view(), name='teacher-list'),
    path('awards/', AwardHome.as_view(), name='award-list'),
    path('license/', show_license, name='license'),
    path('studu_programm/', show_study_program, name='study-programm'),
    path('inn/', show_inn, name='inn'),
    path('timetable/', show_timetable, name='timetable'),
    path('graduates/', show_graduates, name='graduates'),
    path('departments/', show_departments, name='departments'),
    path('charter/', show_charter, name='charter'),
    path('classrooms/', show_classrooms, name='classrooms'),
    path('students/', show_students, name='students'),
    path('news/<int:news_id>/', show_news, name='news'),
    path('poster/<int:poster_id>/', show_poster, name='posters'),
    path('work/<int:work_id>/', show_work, name='works'),
    path('award/<int:award_id>/', show_award, name='award'),
    path('teacher/<int:teacher_id>/', show_teacher, name='teacher'),
    path('delete_poster/<int:poster_id>', delete_poster, name='delete-poster'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
