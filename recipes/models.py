from django.db import models
from django.contrib.auth.models import User
from karzinka.models import Tags


class Recipes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=201)
    description = models.TextField()
    tags = models.ManyToManyField(Tags)
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT = (
        (0, 'gram'),
        (1, 'kg'),
        (2, 'liter'),
        (3, 'pc')
    )
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ingredient')
    title = models.CharField(max_length=201)
    quantity = models.IntegerField()
    unit = models.IntegerField(choices=UNIT)

    def __str__(self):
        return self.title
