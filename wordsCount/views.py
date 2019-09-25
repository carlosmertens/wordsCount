from django.shortcuts import render


def home(request):
    """Funtion to return home page."""

    return render(request, 'home.html')


def count(request):
    """Function to return count page."""

    return render(request, 'count.html')
