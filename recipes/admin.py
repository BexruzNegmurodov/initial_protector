from django.contrib import admin
from .models import Recipes, Ingredient


class IngredientInlineAdmin(admin.TabularInline):
    model = Ingredient
    extra = 1


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    inlines = (IngredientInlineAdmin,)
    list_display = ('id', 'author', 'title', 'ingredient', 'modified_date')
    list_display_links = ('id', 'title')
    filter_horizontal = ('tags',)
    fields = ('author', 'title', 'tags', 'description', "modified_date", 'created_date')
    readonly_fields = ("modified_date", 'created_date')
    search_fields = ('title', 'author__username')
    list_filter = ('modified_date',)
    date_hierarchy = 'modified_date'
    list_per_page = 20

    def ingredient(self, obj):
        return obj.ingredient.count()


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipe', 'title', 'unit', 'quantity')
    search_fields = ('title', 'recipe__title')
    autocomplete_fields = ('recipe',)
