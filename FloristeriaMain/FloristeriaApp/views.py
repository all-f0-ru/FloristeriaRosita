from django.shortcuts import render


def home(request):
    """Renderiza la página principal de Floristería Rosita."""
    return render(request, "FloristeriaApp/home.html")
