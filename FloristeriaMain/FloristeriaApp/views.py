from django.shortcuts import render


def home(request):
    """Renderiza la página principal de Floristería Rosita."""
    return render(request, "FloristeriaApp/home.html")


def login_view(request):
    """Muestra el formulario de inicio de sesión."""
    return render(request, "FloristeriaApp/login.html")


def carrito(request):
    """Presenta el carro de compras."""
    return render(request, "FloristeriaApp/carrito.html")


def contacto(request):
    """Muestra el formulario de contacto."""
    return render(request, "FloristeriaApp/contacto.html")
