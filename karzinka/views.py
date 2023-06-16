from django.shortcuts import render, redirect, reverse
from .models import Karzinka, Category, Tags
from .forms import KarzinkaForm
from django.http import Http404, HttpResponseForbidden
from django.contrib import messages
from django.core.paginator import Paginator


def home(request):
    objs = Karzinka.objects.all()
    objs1 = Karzinka.objects.all()
    category = Category.objects.all()
    tags = Tags.objects.all()
    q = request.GET.get('q')
    cat = request.GET.get('cat')
    tag = request.GET.get('tag')
    if tag:
        objs = objs.filter(tags__id__exact=tag)
    if cat:
        objs = objs.filter(category__id__exact=cat)
    if q:
        objs = objs.filter(name__contains=q)
    paginator = Paginator(objs, 2)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    ctx = {
        'obj': page_obj,
        'obj1': objs1,
        'category': category,
        'tags': tags,

    }
    return render(request, 'karzinka/home.html', ctx)


def detail(request, slug):
    if slug == "None":
        return HttpResponseForbidden('the object is not attribute "slug" ')
    obj = Karzinka.objects.get(slug=slug)
    ctx = {
        'obj': obj
    }
    return render(request, 'karzinka/detail.html', ctx)


def create(request):
    form = KarzinkaForm()
    if request.method == "POST":
        form = KarzinkaForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save()
            messages.success(request, "New file added")
            return redirect(reverse('karzinka:detail', kwargs={'pk': obj.id}))
    ctx = {
        'form': form
    }
    return render(request, 'karzinka/create.html', ctx)


def edit(request, pk):
    try:
        obj = Karzinka.objects.get(id=pk)
    except:
        raise Http404
    form = KarzinkaForm(instance=obj)
    if request.method == "POST":
        form = KarzinkaForm(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.info(request, 'file has been modified')
            return redirect(reverse('karzinka:detail', kwargs={'pk', obj.id}))
    ctx = {
        'form': form
    }
    return render(request, 'karzinka/create.html', ctx)


def delete(request, pk):
    try:
        obj = Karzinka.objects.get(id=pk)
    except:
        raise Http404
    if request.method == "POST":
        obj.delete()
        messages.error(request, 'file has been deleted')
        return redirect('karzinka:home')
    ctx = {
        'obj': obj
    }
    return render(request, 'karzinka/delete.html', ctx)
