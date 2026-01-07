from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    ProveedorFarmacia, Farmaceutico, ClienteFarmacia, 
    Medicamento, RecetaMedica, VentaFarmacia, DetalleVentaFarmacia
)

def inicio_farmacia(request):
    return render(request, 'inicio.html')

# ==========================================
# SECCIÓN CLIENTES (Ya estaba lista)
# ==========================================
def ver_clientes(request):
    clientes = ClienteFarmacia.objects.all()
    return render(request, 'cliente/ver_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        ClienteFarmacia.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion=request.POST.get('direccion'),
            fecha_registro=request.POST.get('fecha_registro'),
            num_seguro_medico=request.POST.get('num_seguro_medico'),
            fecha_nacimiento=request.POST.get('fecha_nacimiento'),
            preferencias=request.POST.get('preferencias')
        )
        return redirect('ver_clientes')
    return render(request, 'cliente/agregar_cliente.html')

def actualizar_cliente(request, id):
    cliente = get_object_or_404(ClienteFarmacia, id=id)
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def realizar_actualizacion_cliente(request, id):
    cliente = get_object_or_404(ClienteFarmacia, id=id)
    if request.method == 'POST':
        cliente.nombre = request.POST.get('nombre')
        cliente.apellido = request.POST.get('apellido')
        cliente.telefono = request.POST.get('telefono')
        cliente.email = request.POST.get('email')
        cliente.direccion = request.POST.get('direccion')
        cliente.fecha_registro = request.POST.get('fecha_registro')
        cliente.num_seguro_medico = request.POST.get('num_seguro_medico')
        cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        cliente.preferencias = request.POST.get('preferencias')
        cliente.save()
        return redirect('ver_clientes')
    return render(request, 'cliente/actualizar_cliente.html', {'cliente': cliente})

def borrar_cliente(request, id):
    cliente = get_object_or_404(ClienteFarmacia, id=id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('ver_clientes')
    return render(request, 'cliente/borrar_cliente.html', {'cliente': cliente})

# ==========================================
# SECCIÓN PROVEEDORES (Ya estaba lista)
# ==========================================
def ver_proveedores(request):
    proveedores = ProveedorFarmacia.objects.all()
    return render(request, 'proveedor/ver_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        ProveedorFarmacia.objects.create(
            nombre_proveedor=request.POST.get('nombre_proveedor'),
            contacto_persona=request.POST.get('contacto_persona'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email'),
            direccion_proveedor=request.POST.get('direccion_proveedor'),
            ruc=request.POST.get('ruc'),
            fecha_registro=request.POST.get('fecha_registro')
        )
        return redirect('ver_proveedores')
    return render(request, 'proveedor/agregar_proveedor.html')

def actualizar_proveedor(request, id):
    proveedor = get_object_or_404(ProveedorFarmacia, id=id)
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def realizar_actualizacion_proveedor(request, id):
    proveedor = get_object_or_404(ProveedorFarmacia, id=id)
    if request.method == 'POST':
        proveedor.nombre_proveedor = request.POST.get('nombre_proveedor')
        proveedor.contacto_persona = request.POST.get('contacto_persona')
        proveedor.telefono = request.POST.get('telefono')
        proveedor.email = request.POST.get('email')
        proveedor.direccion_proveedor = request.POST.get('direccion_proveedor')
        proveedor.ruc = request.POST.get('ruc')
        proveedor.fecha_registro = request.POST.get('fecha_registro')
        proveedor.save()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/actualizar_proveedor.html', {'proveedor': proveedor})

def borrar_proveedor(request, id):
    proveedor = get_object_or_404(ProveedorFarmacia, id=id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('ver_proveedores')
    return render(request, 'proveedor/borrar_proveedor.html', {'proveedor': proveedor})

# ==========================================
# SECCIÓN MEDICAMENTOS (Ya estaba lista)
# ==========================================
def ver_medicamentos(request):
    medicamentos = Medicamento.objects.all()
    return render(request, 'medicamento/ver_medicamentos.html', {'medicamentos': medicamentos})

def agregar_medicamento(request):
    proveedores = ProveedorFarmacia.objects.all()
    if request.method == 'POST':
        prov_obj = get_object_or_404(ProveedorFarmacia, id=request.POST.get('proveedor'))
        Medicamento.objects.create(
            nombre_medicamento=request.POST.get('nombre_medicamento'),
            descripcion=request.POST.get('descripcion'),
            precio_venta=request.POST.get('precio_venta'),
            stock=request.POST.get('stock'),
            fecha_vencimiento=request.POST.get('fecha_vencimiento'),
            codigo_barra=request.POST.get('codigo_barra'),
            principio_activo=request.POST.get('principio_activo'),
            forma_farmaceutica=request.POST.get('forma_farmaceutica'),
            requiere_receta=request.POST.get('requiere_receta') == 'on',
            proveedor=prov_obj
        )
        return redirect('ver_medicamentos')
    return render(request, 'medicamento/agregar_medicamento.html', {'proveedores': proveedores})

def actualizar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    proveedores = ProveedorFarmacia.objects.all()
    return render(request, 'medicamento/actualizar_medicamento.html', {'medicamento': medicamento, 'proveedores': proveedores})

def realizar_actualizacion_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    proveedores = ProveedorFarmacia.objects.all()
    if request.method == 'POST':
        medicamento.proveedor = get_object_or_404(ProveedorFarmacia, id=request.POST.get('proveedor'))
        medicamento.nombre_medicamento = request.POST.get('nombre_medicamento')
        medicamento.descripcion = request.POST.get('descripcion')
        medicamento.precio_venta = request.POST.get('precio_venta')
        medicamento.stock = request.POST.get('stock')
        medicamento.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        medicamento.codigo_barra = request.POST.get('codigo_barra')
        medicamento.principio_activo = request.POST.get('principio_activo')
        medicamento.forma_farmaceutica = request.POST.get('forma_farmaceutica')
        medicamento.requiere_receta = request.POST.get('requiere_receta') == 'on'
        medicamento.save()
        return redirect('ver_medicamentos')
    return render(request, 'medicamento/actualizar_medicamento.html', {'medicamento': medicamento, 'proveedores': proveedores})

def borrar_medicamento(request, id):
    medicamento = get_object_or_404(Medicamento, id=id)
    if request.method == 'POST':
        medicamento.delete()
        return redirect('ver_medicamentos')
    return render(request, 'medicamento/borrar_medicamento.html', {'medicamento': medicamento})

# ==========================================
# SECCIÓN FARMACÉUTICOS (CORREGIDO)
# ==========================================
def ver_farmaceuticos(request):
    farmaceuticos = Farmaceutico.objects.all()
    return render(request, 'farmaceutico/ver_farmaceuticos.html', {'farmaceuticos': farmaceuticos})

def agregar_farmaceutico(request):
    if request.method == 'POST':
        Farmaceutico.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            dni=request.POST.get('dni'),
            fecha_contratacion=request.POST.get('fecha_contratacion'),
            salario=request.POST.get('salario'),
            licencia_colegiado=request.POST.get('licencia_colegiado'),
            turno=request.POST.get('turno'),
            telefono=request.POST.get('telefono'),
            email=request.POST.get('email')
        )
        return redirect('ver_farmaceuticos')
    return render(request, 'farmaceutico/agregar_farmaceutico.html')

def actualizar_farmaceutico(request, id):
    farmaceutico = get_object_or_404(Farmaceutico, id=id)
    return render(request, 'farmaceutico/actualizar_farmaceutico.html', {'farmaceutico': farmaceutico})

def realizar_actualizacion_farmaceutico(request, id):
    farmaceutico = get_object_or_404(Farmaceutico, id=id)
    if request.method == 'POST':
        farmaceutico.nombre = request.POST.get('nombre')
        farmaceutico.apellido = request.POST.get('apellido')
        farmaceutico.dni = request.POST.get('dni')
        farmaceutico.fecha_contratacion = request.POST.get('fecha_contratacion')
        farmaceutico.salario = request.POST.get('salario')
        farmaceutico.licencia_colegiado = request.POST.get('licencia_colegiado')
        farmaceutico.turno = request.POST.get('turno')
        farmaceutico.telefono = request.POST.get('telefono')
        farmaceutico.email = request.POST.get('email')
        farmaceutico.save()
        return redirect('ver_farmaceuticos')
    return render(request, 'farmaceutico/actualizar_farmaceutico.html', {'farmaceutico': farmaceutico})

def borrar_farmaceutico(request, id):
    farmaceutico = get_object_or_404(Farmaceutico, id=id)
    if request.method == 'POST':
        farmaceutico.delete()
        return redirect('ver_farmaceuticos')
    return render(request, 'farmaceutico/borrar_farmaceutico.html', {'farmaceutico': farmaceutico})

# ==========================================
# SECCIÓN VENTAS (CORREGIDO)
# ==========================================
def ver_ventas(request):
    ventas = VentaFarmacia.objects.all()
    return render(request, 'venta/ver_ventas.html', {'ventas': ventas})

def agregar_venta(request):
    clientes = ClienteFarmacia.objects.all()
    farmaceuticos = Farmaceutico.objects.all()
    if request.method == 'POST':
        cli = get_object_or_404(ClienteFarmacia, id=request.POST.get('cliente'))
        farm = get_object_or_404(Farmaceutico, id=request.POST.get('farmaceutico'))
        VentaFarmacia.objects.create(
            fecha_venta=request.POST.get('fecha_venta'),
            total_venta=request.POST.get('total_venta'),
            metodo_pago=request.POST.get('metodo_pago'),
            descuento_total=request.POST.get('descuento_total'),
            numero_factura=request.POST.get('numero_factura'),
            estado_venta=request.POST.get('estado_venta'),
            cliente=cli,
            farmaceutico=farm
        )
        return redirect('ver_ventas')
    return render(request, 'venta/agregar_venta.html', {'clientes': clientes, 'farmaceuticos': farmaceuticos})

def actualizar_venta(request, id):
    venta = get_object_or_404(VentaFarmacia, id=id)
    clientes = ClienteFarmacia.objects.all()
    farmaceuticos = Farmaceutico.objects.all()
    return render(request, 'venta/actualizar_venta.html', {'venta': venta, 'clientes': clientes, 'farmaceuticos': farmaceuticos})

def realizar_actualizacion_venta(request, id):
    venta = get_object_or_404(VentaFarmacia, id=id)
    clientes = ClienteFarmacia.objects.all()
    farmaceuticos = Farmaceutico.objects.all()
    if request.method == 'POST':
        venta.cliente = get_object_or_404(ClienteFarmacia, id=request.POST.get('cliente'))
        venta.farmaceutico = get_object_or_404(Farmaceutico, id=request.POST.get('farmaceutico'))
        venta.fecha_venta = request.POST.get('fecha_venta')
        venta.total_venta = request.POST.get('total_venta')
        venta.metodo_pago = request.POST.get('metodo_pago')
        venta.descuento_total = request.POST.get('descuento_total')
        venta.numero_factura = request.POST.get('numero_factura')
        venta.estado_venta = request.POST.get('estado_venta')
        venta.save()
        return redirect('ver_ventas')
    return render(request, 'venta/actualizar_venta.html', {'venta': venta, 'clientes': clientes, 'farmaceuticos': farmaceuticos})

def borrar_venta(request, id):
    venta = get_object_or_404(VentaFarmacia, id=id)
    if request.method == 'POST':
        venta.delete()
        return redirect('ver_ventas')
    return render(request, 'venta/borrar_venta.html', {'venta': venta})

# ==========================================
# SECCIÓN DETALLES VENTA (CORREGIDO)
# ==========================================
def ver_detalles(request):
    detalles = DetalleVentaFarmacia.objects.all()
    return render(request, 'detalle/ver_detalles.html', {'detalles': detalles})

def agregar_detalle(request):
    ventas = VentaFarmacia.objects.all()
    medicamentos = Medicamento.objects.all()
    if request.method == 'POST':
        ven = get_object_or_404(VentaFarmacia, id=request.POST.get('venta'))
        med = get_object_or_404(Medicamento, id=request.POST.get('medicamento'))
        DetalleVentaFarmacia.objects.create(
            venta=ven,
            medicamento=med,
            cantidad=request.POST.get('cantidad'),
            precio_unitario_venta=request.POST.get('precio_unitario_venta'),
            subtotal=request.POST.get('subtotal'),
            iva_aplicado=request.POST.get('iva_aplicado')
        )
        return redirect('ver_detalles')
    return render(request, 'detalle/agregar_detalle.html', {'ventas': ventas, 'medicamentos': medicamentos})

def actualizar_detalle(request, id):
    detalle = get_object_or_404(DetalleVentaFarmacia, id=id)
    ventas = VentaFarmacia.objects.all()
    medicamentos = Medicamento.objects.all()
    return render(request, 'detalle/actualizar_detalle.html', {'detalle': detalle, 'ventas': ventas, 'medicamentos': medicamentos})

def realizar_actualizacion_detalle(request, id):
    detalle = get_object_or_404(DetalleVentaFarmacia, id=id)
    ventas = VentaFarmacia.objects.all()
    medicamentos = Medicamento.objects.all()
    if request.method == 'POST':
        detalle.venta = get_object_or_404(VentaFarmacia, id=request.POST.get('venta'))
        detalle.medicamento = get_object_or_404(Medicamento, id=request.POST.get('medicamento'))
        detalle.cantidad = request.POST.get('cantidad')
        detalle.precio_unitario_venta = request.POST.get('precio_unitario_venta')
        detalle.subtotal = request.POST.get('subtotal')
        detalle.iva_aplicado = request.POST.get('iva_aplicado')
        detalle.save()
        return redirect('ver_detalles')
    return render(request, 'detalle/actualizar_detalle.html', {'detalle': detalle, 'ventas': ventas, 'medicamentos': medicamentos})

def borrar_detalle(request, id):
    detalle = get_object_or_404(DetalleVentaFarmacia, id=id)
    if request.method == 'POST':
        detalle.delete()
        return redirect('ver_detalles')
    return render(request, 'detalle/borrar_detalle.html', {'detalle': detalle})

# ==========================================
# SECCIÓN RECETAS (CORREGIDO)
# ==========================================
def ver_recetas(request):
    recetas = RecetaMedica.objects.all()
    return render(request, 'receta/ver_recetas.html', {'recetas': recetas})

def agregar_receta(request):
    clientes = ClienteFarmacia.objects.all()
    if request.method == 'POST':
        cli = get_object_or_404(ClienteFarmacia, id=request.POST.get('cliente'))
        RecetaMedica.objects.create(
            cliente=cli,
            id_medico_receto=request.POST.get('id_medico_receto'),
            fecha_emision=request.POST.get('fecha_emision'),
            fecha_vencimiento=request.POST.get('fecha_vencimiento'),
            diagnostico=request.POST.get('diagnostico'),
            medicamento_recetado_texto=request.POST.get('medicamento_recetado_texto'),
            dosis_indicada=request.POST.get('dosis_indicada'),
            estado_receta=request.POST.get('estado_receta')
        )
        return redirect('ver_recetas')
    return render(request, 'receta/agregar_receta.html', {'clientes': clientes})

def actualizar_receta(request, id):
    receta = get_object_or_404(RecetaMedica, id=id)
    clientes = ClienteFarmacia.objects.all()
    return render(request, 'receta/actualizar_receta.html', {'receta': receta, 'clientes': clientes})

def realizar_actualizacion_receta(request, id):
    receta = get_object_or_404(RecetaMedica, id=id)
    clientes = ClienteFarmacia.objects.all()
    if request.method == 'POST':
        receta.cliente = get_object_or_404(ClienteFarmacia, id=request.POST.get('cliente'))
        receta.id_medico_receto = request.POST.get('id_medico_receto')
        receta.fecha_emision = request.POST.get('fecha_emision')
        receta.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        receta.diagnostico = request.POST.get('diagnostico')
        receta.medicamento_recetado_texto = request.POST.get('medicamento_recetado_texto')
        receta.dosis_indicada = request.POST.get('dosis_indicada')
        receta.estado_receta = request.POST.get('estado_receta')
        receta.save()
        return redirect('ver_recetas')
    return render(request, 'receta/actualizar_receta.html', {'receta': receta, 'clientes': clientes})

def borrar_receta(request, id):
    receta = get_object_or_404(RecetaMedica, id=id)
    if request.method == 'POST':
        receta.delete()
        return redirect('ver_recetas')
    return render(request, 'receta/borrar_receta.html', {'receta': receta})
