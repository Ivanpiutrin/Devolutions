from django.shortcuts import render
from devoluciones.models import DevolucionCliente


def ingresarDev(request):
    devClient = DevolucionCliente.objects.all()
    data ={'devClient':devClient}
    return render(request,'devolucion.html', data)

# Create your views here.
def CrearDev(request):
    d_rut = request.POST['txt_rut']
    d_nombre = request.POST['txt_nombre']
    d_email = request.POST['txt_email']
    d_celular = request.POST['txt_celular']
    d_cantidad = request.POST['txt_cantidad']
    d_producto = request.POST['txt_producto']
    d_nombrevendedor = request.POST['txt_nombrevendedor']
    d_distribuidor = request.POST['txt_distribuidor']
    d_direccion = request.POST['txt_direccion']


    devolucion = DevolucionCliente(rut = d_rut, nombre = d_nombre, email = d_email, celular = d_celular, cantidad = d_cantidad,
                                    producto = d_producto, NombreVendedor = d_nombrevendedor, distribuidor = d_distribuidor, direccion = d_direccion)

    devolucion.save()                                


    return render(request,'Confirmacion.html')