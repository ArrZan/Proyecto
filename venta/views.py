from django.shortcuts import render, HttpResponse

# Create your views here.
html = """
 <h1>Shopping car</h1>
 <ul>
 <li><a href="/">Inicio</a></li>
 <li><a href="/articulo">Articulos</a></li>
 <li><a href="/cliente">Clientes</a></li>
 <li><a href="/venta">Ventas</a></li>
 </ul>"""

def inicio(request):
    return HttpResponse(html+"<h1>Mi primera web de Django!</h1>")

def articulo(request):
    nombre = "Erly Naranjo"
    return render(request, 'Cliente/formClientes.html',{"usuario":nombre})
def cliente(request):
    return HttpResponse(html+"""<h1>Mantenimiento de Clientes</h1>""")

def venta(request):
    return HttpResponse(html+"""<h1>Venta de Articulos</h1>""")