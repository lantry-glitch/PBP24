from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152134',
        'name': 'Allan Kwek',
        'class': 'PBP F',
        'aplikasi': 'ParKing',
        'slogan': 'Rule Your Parking Experience',
        'deskripsi': 'aplikasi review dan live-update ketersediaan tempat parkir'
    }

    return render(request, "main.html", context)
