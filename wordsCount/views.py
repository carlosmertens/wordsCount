from django.http import HttpResponse


def home(request):
    """Funtion to return "Hello Amigos!!!."""

    return HttpResponse('Hello Amigos!!!')
