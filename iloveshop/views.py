from itertools import product
from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpRequest, response, Http404, HttpResponseRedirect
from django.urls import path

from .models import Question
from .models import ILoveModels

from .forms import ILoveForm

from django.utils import timezone



def create_view(request) :
    context ={}

    form = ILoveForm(request.POST or None)
    if form.is_valid() :
        form.save()

    context['form']= form
    context["dataset"] = ILoveModels.objects.all().filter( {{data.stock}} > 0)

    return render(request, "iloveshop/index.html", context)

def detail_view(request, id):

    context ={}

    context["data"] = ILoveModels.objects.get(id = id)
    product = get_object_or_404(ILoveModels, id = id)
    form = ILoveForm(request.POST or None, instance = product)
    
    if form.is_valid():
        product.delete()
        return redirect("/iloveshop")
         
    return render(request, "iloveshop/detail_view.html", context)

def update_view(request, id):

    context ={}
 

    obj = get_object_or_404(ILoveModels, id = id)

    form = ILoveForm(request.POST or None, instance = obj)
 

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/iloveshop/"+id)


 
    context["form"] = form
 
    return render(request, "iloveshop/update_view.html", context)


def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(ILoveModels, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/iloveshop")
 
    return render(request, "iloveshop/delete_view.html", context)