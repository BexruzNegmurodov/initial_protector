from django.urls import path
from .views import recipes_list, create, detail, edit, delete, ingredient_create, ingredient_edit, ingredient_delete

app_name = 'recipes'

urlpatterns = [
    path('recipes_list/', recipes_list, name='list'),
    path('create_recipes/', create, name='create'),
    path('detail_recipes/<int:pk>', detail, name='detail'),
    path('edit_recipes/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete'),
    path('<int:recipe_id>/ingredient/create', ingredient_create, name='ing_create'),
    path('<int:recipe_id>/ingredient/edit/<int:pk>', ingredient_edit, name='ing_edit'),
    path('<int:recipe_id>/ingredient/delete/<int:pk>', ingredient_delete, name='ing_delete'),
]
