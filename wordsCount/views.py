from django.shortcuts import render


def home(request):
    """Funtion to return home page."""

    return render(request, 'home.html')
