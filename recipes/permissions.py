from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import Recipes, Ingredient


def owner_required(class_):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            # Retrieve the object being accessed
            obj = get_object_or_404(class_, id=kwargs['pk'])

            # Check if the authenticated user is the owner of the object
            if obj.author != request.user:
                return HttpResponseForbidden("You are not the owner of this object.")

            # Call the view function if the user is the owner
            return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator


def owner_required_ing(class_):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            # Retrieve the object being accessed
            obj = get_object_or_404(class_, id=kwargs['pk'])

            # Check if the authenticated user is the owner of the object
            if obj.recipe.author != request.user:
                return HttpResponseForbidden("You are not the owner of this object.")

            # Call the view function if the user is the owner
            return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator
