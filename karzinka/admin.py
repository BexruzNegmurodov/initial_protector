from django.contrib import admin
from .models import Karzinka, Category, Tags


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class KarzinkaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category')
    fields = ('name', 'slug', 'category', 'image', 'information', 'tags', 'created_date')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_date',)
    search_fields = ('name',)
    filter_horizontal = ('tags',)
    list_filter = ('created_date', 'category')
    list_editable = ('category',)


admin.site.register(Karzinka, KarzinkaAdmin)
