from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from .models import Karzinka


def karzinka_pre_save(instance, sender, *args, **kwargs):
    if instance.slug is None:
        instance.slug = slugify(instance.name)
    return instance


pre_save.connect(karzinka_pre_save, sender=Karzinka)
