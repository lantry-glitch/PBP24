import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from main.forms import ParKingEntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def show_main(request):
    park_entries = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2306152134',
        'name': request.user.username,
        'class': 'PBP F',
        'aplikasi': 'ParKing',
        'slogan': 'Rule Your Parking Experience',
        'deskripsi': 'aplikasi review dan live-update kondisi ketersediaan tempat parkir beserta harganya',
        'park_entries': park_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_park_entry(request):
    form = ParKingEntryForm(request.POST or None, request.FILES)

    if form.is_valid() and request.method == "POST":
        park_entry = form.save(commit=False)
        park_entry.user = request.user
        park_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_park_entry.html", context)

def edit_park(request, id):
    # Get mood entry berdasarkan id
    park = Product.objects.get(pk = id)

    # Set mood entry sebagai instance dari form
    form = ParKingEntryForm(request.POST or None, instance=park)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_park.html", context)

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

def delete_park(request, id):
    # Get mood berdasarkan id
    park = Product.objects.get(pk = id)
    # Hapus mood
    park.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response