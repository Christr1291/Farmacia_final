from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_farmacia, name='inicio_farmacia'),

    # Clientes
    path('clientes/', views.ver_clientes, name='ver_clientes'),
    path('clientes/agregar/', views.agregar_cliente, name='agregar_cliente'),
    path('clientes/actualizar/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('clientes/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_cliente, name='realizar_actualizacion_cliente'),
    path('clientes/borrar/<int:id>/', views.borrar_cliente, name='borrar_cliente'),

    # Proveedores
    path('proveedores/', views.ver_proveedores, name='ver_proveedores'),
    path('proveedores/agregar/', views.agregar_proveedor, name='agregar_proveedor'),
    path('proveedores/actualizar/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('proveedores/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_proveedor, name='realizar_actualizacion_proveedor'),
    path('proveedores/borrar/<int:id>/', views.borrar_proveedor, name='borrar_proveedor'),

    # Medicamentos
    path('medicamentos/', views.ver_medicamentos, name='ver_medicamentos'),
    path('medicamentos/agregar/', views.agregar_medicamento, name='agregar_medicamento'),
    path('medicamentos/actualizar/<int:id>/', views.actualizar_medicamento, name='actualizar_medicamento'),
    path('medicamentos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_medicamento, name='realizar_actualizacion_medicamento'),
    path('medicamentos/borrar/<int:id>/', views.borrar_medicamento, name='borrar_medicamento'),

    # Farmacéuticos
    path('farmaceuticos/', views.ver_farmaceuticos, name='ver_farmaceuticos'),
    path('farmaceuticos/agregar/', views.agregar_farmaceutico, name='agregar_farmaceutico'),
    path('farmaceuticos/actualizar/<int:id>/', views.actualizar_farmaceutico, name='actualizar_farmaceutico'),
    path('farmaceuticos/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_farmaceutico, name='realizar_actualizacion_farmaceutico'),
    path('farmaceuticos/borrar/<int:id>/', views.borrar_farmaceutico, name='borrar_farmaceutico'),

    # Ventas
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/actualizar/<int:id>/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('ventas/borrar/<int:id>/', views.borrar_venta, name='borrar_venta'),

    # Detalles Venta
    path('detalles/', views.ver_detalles, name='ver_detalles'),
    path('detalles/agregar/', views.agregar_detalle, name='agregar_detalle'),
    path('detalles/actualizar/<int:id>/', views.actualizar_detalle, name='actualizar_detalle'),
    path('detalles/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_detalle, name='realizar_actualizacion_detalle'),
    path('detalles/borrar/<int:id>/', views.borrar_detalle, name='borrar_detalle'),

    # Recetas
    path('recetas/', views.ver_recetas, name='ver_recetas'),
    path('recetas/agregar/', views.agregar_receta, name='agregar_receta'),
    path('recetas/actualizar/<int:id>/', views.actualizar_receta, name='actualizar_receta'),
    path('recetas/realizar_actualizacion/<int:id>/', views.realizar_actualizacion_receta, name='realizar_actualizacion_receta'),
    path('recetas/borrar/<int:id>/', views.borrar_receta, name='borrar_receta'),
]