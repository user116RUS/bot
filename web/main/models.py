from django.db import models

# Create your models here.
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    text = models.TextField(blank=False, verbose_name='Текст публикации')
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ['date', 'title']


class Poster(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    '''slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')'''
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    date_provide = models.DateTimeField(auto_now_add=False, verbose_name='Дата проведения')
    text_short = models.TextField(blank=False, max_length=40, verbose_name='Короткий текст описания')
    text = models.TextField(blank=True, verbose_name='Текст публикации')
    photo = models.ImageField(upload_to="photo/posters/%Y/%m/%d/", verbose_name='Фото')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('poster', kwargs={'poster_id': self.pk})

    class Meta:
        verbose_name = "Афиша"
        verbose_name_plural = "Афиши"
        ordering = ['date', 'title']


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    info = models.TextField(blank=True, verbose_name='Информация')
    photo = models.ImageField(upload_to="photo/children/%Y/%m/%d/", verbose_name='Фото (необязательно)', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Child(User):
    form = models.CharField(max_length=10, verbose_name='Класс')

    class Meta:
        verbose_name = "Ученик"
        verbose_name_plural = "Ученики"
        ordering = ['form', 'name']


class Teacher(User):
    subject = models.CharField(max_length=20, verbose_name='Предмет')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('teacher', kwargs={'teacher_id': self.pk})

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ['name']


class Work(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Название работы')
    photo = models.ImageField(upload_to='work/photo/%Y/%m/%d', verbose_name='Фото Работы')
    author = models.CharField(max_length=255, blank=False, verbose_name='Автор' )
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.author

    def get_absolute_url(self):
        return reverse('work', kwargs={'work_id': self.pk})

    class Meta:
        verbose_name = "Работа ученика"
        verbose_name_plural = "Работы учеников"
        ordering = ['name']


class Docs(models.Model):
    studyProgram = models.FileField(upload_to='files/studyProgram/%Y/%m/%d/', verbose_name='Образовательная программа')
    timetable = models.FileField(upload_to="photo/children/%Y/%m/%d/", verbose_name='Расписание')
    graduates = models.FileField(upload_to='files/graduates/%Y/%m/%d/', verbose_name='Список выпускников')
    departments = models.FileField(upload_to='files/departments/%Y/%m/%d/', verbose_name='Количество отделений')
    charter = models.FileField(upload_to='files/charter/%Y/%m/%d/', verbose_name='Устав школы')
    inn = models.FileField(upload_to='files/inn/%Y/%m/%d/', verbose_name='ИНН')
    classrooms = models.FileField(upload_to='files/classrooms/%Y/%m/%d/', verbose_name='СПИСОК УЧЕБНЫХ КЛАССОВ')
    datetime = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    students = models.FileField(upload_to='files/pupil/%Y/%m/%d/', verbose_name='Список учащихся', default='DEFAULT VALUE')

    def get_absolute_url(self):
        return reverse('document', kwargs={'document_id': self.pk})

    class Meta:
        verbose_name = "Докментация"
        verbose_name_plural = "Документации"
        ordering = ['datetime']


class License(models.Model):
    licens = models.FileField(upload_to='files/licens/%Y/%m/%d/', verbose_name='Лицензия лист ')
    datetime = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def get_absolute_url(self):
        return reverse('license', kwargs={'license_id': self.pk})

    class Meta:
        verbose_name = "Лист лицензии"
        verbose_name_plural = "Лицензия"
        ordering = ['datetime']


class Award(models.Model):
    owner = models.CharField(max_length=100, verbose_name='Получил')
    photo = models.ImageField(upload_to='photo/work/%Y/%m/%d', verbose_name='Фото Награды')
    describe = models.TextField(blank=True, verbose_name='Описание (необязательно)')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    def __str__(self):
        return self.owner

    def get_absolute_url(self):
        return reverse('award', kwargs={'award_id': self.pk})

    class Meta:
        verbose_name = "Награда ученика"
        verbose_name_plural = "Награды учеников"
        ordering = ['owner']



