from django.contrib import admin

# Register your models here.
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_display_links = ('title', )
    search_fields = ('title', 'text')
    list_filter = ('date', )


class PosterAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_provide', )
    list_display_links = ('title', )
    search_fields = ('title', 'text', )
    list_filter = ('date_provide', )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', )
    list_display_links = ('name',)
    search_fields = ('name', 'info', 'subject')
    list_filter = ('subject',)


class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'form', )
    list_display_links = ('name',)
    search_fields = ('name', 'info', )
    list_filter = ('form',)


class AwardsAdmin(admin.ModelAdmin):
    list_display = ('owner', 'date')
    list_display_links = ('owner',)
    search_fields = ('owner', 'describe',)
    list_filter = ('date',)


class WorkAdmin(admin.ModelAdmin):
    list_display = ('author', 'name', 'date',)
    list_display_links = ('author',)
    search_fields = ('name', 'name',)
    list_filter = ('date',)


class DocsAdmin(admin.ModelAdmin):
    list_display = ('datetime',)
    list_display_links = ('datetime',)
    search_fields = ('datetime',)
    list_filter = ('datetime',)


class LicenseAdmin(admin.ModelAdmin):
    list_display = ('datetime',)
    list_display_links = ('datetime',)
    search_fields = ('datetime',)
    list_filter = ('datetime',)


admin.site.register(License, LicenseAdmin)
admin.site.register(Docs, DocsAdmin)
admin.site.register(Award, AwardsAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Poster, PosterAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Child, ChildAdmin)
