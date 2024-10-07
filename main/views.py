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
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):

    context = {
        'npm' : '2306152134',
        'name': request.user.username,
        'class': 'PBP F',
        'aplikasi': 'ParKing',
        'slogan': 'Rule Your Parking Experience',
        'deskripsi': 'aplikasi review dan live-update kondisi ketersediaan tempat parkir beserta harganya',
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

@csrf_exempt
@require_POST
def add_park_entry_ajax(request):
    nama = strip_tags(request.POST.get("nama"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    rating = request.POST.get("rating")
    quantity = request.POST.get("quantity")
    user = request.user

    new_park = Product(
        nama=nama, price=price, description=description,
        rating=rating,quantity=quantity,
        user=user
    )
    new_park.save()

    return HttpResponse(b"CREATED", status=201)

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
    data = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.filter(user=request.user)
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
      messages.error(request, "Invalid username or password. Please try again.")
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response