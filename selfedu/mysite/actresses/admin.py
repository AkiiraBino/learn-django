from django.contrib import admin
from actresses import models

class ActressesAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'photo', 'is_published')
    list_display_links = ('title',)
    search_fields = ('title', 'content')
    list_editable = ('is_published', )
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title', )}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(models.Actresses, ActressesAdmin)
admin.site.register(models.Category, CategoryAdmin)