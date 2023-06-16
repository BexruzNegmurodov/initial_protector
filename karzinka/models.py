from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    # karzinka_set
    @property
    def category_count(self):
        return self.karzinka.count()


class Tags(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Karzinka(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, unique=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="karzinka")
    image = models.ImageField(null=True, blank=True, upload_to='image')
    information = models.TextField()
    tags = models.ManyToManyField(Tags, )
    created_date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.name


