from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import Http404
from django.contrib import messages


from .models import Recipes, Ingredient, Tags
from .forms import RecipesForm, IngredientForm
from .permissions import owner_required, owner_required_ing

app_name = 'recipes'


def recipes_list(request):
    recipes = Recipes.objects.all().order_by('-id')
    recipes1 = Recipes.objects.all()
    tags = Tags.objects.all()
    tag = request.GET.get('tag')
    if tag:
        recipes = recipes.filter(tags__title__exact=tag)
    ctx = {
        'recipes': recipes,
        'tags': tags,
        'recipes1': recipes1
    }
    return render(request, 'recipes/list.html', ctx)


@login_required(login_url=settings.LOGIN_URL)
def create(request):
    # if not request.user.is_authenticated:
    #     text = request.path
    #     full_path = f"{reverse('account:login')}?next={text}"
    #     return redirect(full_path)
    form = RecipesForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        form.save_m2m()
        return redirect('recipes:list')
    ctx = {
        'form': form
    }
    return render(request, 'recipes/create.html', ctx)


def detail(request, pk):
    # obj = get_object_or_404(Recipes, pk)
    try:
        obj = Recipes.objects.get(id=pk)
        print(obj)
    except:
        raise Http404
    ctx = {
        'obj': obj
    }
    return render(request, 'recipes/detail.html', ctx)


@login_required(login_url=settings.LOGIN_URL)
@owner_required(Recipes)
def edit(request, pk):
    obj = get_object_or_404(Recipes, id=pk)
    form = RecipesForm(instance=obj)
    if request.method == "POST":
        form = RecipesForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('recipes:detail', kwargs={'pk': pk}))
    ctx = {
        'form': form
    }
    return render(request, 'recipes/create.html', ctx)


@owner_required(Recipes)
def delete(request, pk):
    obj = get_object_or_404(Recipes, id=pk)

    if request.method == "POST":
        obj.delete()
        return redirect('recipes:list')
    ctx = {
        'obj': obj
    }
    return render(request, 'recipes/detele.html', ctx)


def ingredient_create(request, recipe_id):
    form = IngredientForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.recipe_id = recipe_id
        obj.save()
        messages.success(request, f'successfully added {obj.title}')
        return redirect(reverse('recipes:detail', kwargs={'pk': recipe_id}))
    ctx = {
        'form': form,
        'recipes_id': recipe_id
    }
    return render(request, 'recipes/ingredient/create.html', ctx)


@owner_required_ing(Ingredient)
def ingredient_edit(request, pk, recipe_id):
    # obj = get_object_or_404(Ingredient, id=pk)
    try:
        obj = Ingredient.objects.get(id=pk)
    except:
        raise Http404
    form = IngredientForm(instance=obj)
    if request.method == "POST":
        form = IngredientForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'edit')
            return redirect(reverse('recipes:detail', kwargs={'pk': recipe_id}))
    ctx = {
        'form': form,
        'recipe_id': recipe_id,
    }
    return render(request, 'recipes/ingredient/create.html', ctx)


@owner_required_ing(Ingredient)
def ingredient_delete(request, recipe_id, pk):
    obj = get_object_or_404(Ingredient, id=pk)
    print(obj)
    if request.method == "POST":
        obj.delete()
        messages.error(request, 'delete')
        return redirect(reverse('recipes:detail', kwargs={'pk': recipe_id}))
    ctx = {
        'obj': obj,
        'recipe_id': recipe_id,
    }
    return render(request, 'recipes/ingredient/delete.html', ctx)
