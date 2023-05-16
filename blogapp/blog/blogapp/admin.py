from django.contrib import admin
from .models import Post
# Register your models here.

#Класс для отображения постов в админке
class PostAdmin(admin.ModelAdmin):
    #Колонки и названия
    list_display = ('title', 'slug', 'author', 'time_publish', 'status')
    #Правая боковая панель для фильтров
    list_filter = ('status', 'time_created', 'time_publish', 'author')
    #Панель поиска по данным атрибутам
    search_fields = ('title', 'body')
    #Автозаполнение слага по  тайтлу
    prepopulated_fields = {'slug': ('title',)}
    #Поиск по авторам, замена автора на id
    raw_id_fields = ('author',)
    #Переход по датам
    date_hierarchy = 'time_publish'
    #Сортировка
    ordering = ['status', 'time_publish']
admin.site.register(Post, PostAdmin)