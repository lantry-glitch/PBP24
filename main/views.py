from django.shortcuts import render, redirect
from main.forms import ParKingEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    park_entries = Product.objects.all()

    context = {
        'npm' : '2306152134',
        'name': 'Allan Kwek',
        'class': 'PBP F',
        'aplikasi': 'ParKing',
        'slogan': 'Rule Your Parking Experience',
        'deskripsi': 'aplikasi review dan live-update kondisi ketersediaan tempat parkir beserta harganya',
        'park_entries': park_entries
    }

    return render(request, "main.html", context)

def create_park_entry(request):
    form = ParKingEntryForm(request.POST or None, request.FILES)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_park_entry.html", context)

def delete_all_entry(request):
    for product in Product.objects.all():
        if product.image:
            product.image.delete(save=False)
    Product.objects.all().delete()
    return redirect("main:show_main")

def delete_last_entry(request):
    last_data = Product.objects.all().last()
    last_data.delete()
    if last_data.image:
            last_data.image.delete(save=False)
    return redirect("main:show_main")

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")