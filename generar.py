import pandas as pd
from datetime import datetime

'''
# Datos de muestra para rellenar la planilla de defectos
defectos = [
    {"ID Defecto": 1, "Descripción": "El campo 'quantity' en el modelo 'Order' no tiene valor por defecto", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Datos", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 2, "Descripción": "La vista 'add_to_cart' no maneja correctamente la cantidad", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 3, "Descripción": "Filtro 'multiply' no registrado correctamente", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Interfaz", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 4, "Descripción": "Error 404 al agregar productos al carrito", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 5, "Descripción": "Productos no se muestran en la tienda", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 6, "Descripción": "Errores de ruteo en URLs", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Sintaxis", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 7, "Descripción": "Problemas en la autenticación y autorización", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 8, "Descripción": "RUT de administradores no validado correctamente", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Datos", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 9, "Descripción": "Botón de agregar al carrito no funciona", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Interfaz", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 10, "Descripción": "Categorías de productos no filtradas correctamente", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 11, "Descripción": "Correo de verificación no enviado al registrar nuevo usuario", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 12, "Descripción": "Error al calcular el total del carrito", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Datos", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 13, "Descripción": "Integración con WebPay no funciona", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 14, "Descripción": "Errores al aprobar/rechazar pedidos", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 15, "Descripción": "Problemas al registrar contadores", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 16, "Descripción": "Error al cambiar contraseña de administradores", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 17, "Descripción": "Estado de pedidos no actualizado correctamente", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 18, "Descripción": "Los bodegueros no pueden aceptar pedidos", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 19, "Descripción": "Problemas al registrar vendedores", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 20, "Descripción": "Problemas al registrar clientes", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 21, "Descripción": "Problema de sincronización de datos en el carrito", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Datos", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 22, "Descripción": "Error en el sistema de notificaciones", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Sistema", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 23, "Descripción": "Problema con el formato de fecha en el checkout", "Severidad": "Leve", "Estado": "Corregido", "Tipo": "Interfaz", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 24, "Descripción": "Problemas con la persistencia de sesiones", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Sistema", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 25, "Descripción": "Error en la validación de direcciones de correo", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Datos", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 26, "Descripción": "Interfaz de usuario no responsiva en dispositivos móviles", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Interfaz", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 27, "Descripción": "Error en el sistema de búsqueda de productos", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 28, "Descripción": "Problemas al procesar pagos con tarjeta de crédito", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 29, "Descripción": "Errores de compatibilidad con ciertos navegadores", "Severidad": "Leve", "Estado": "Corregido", "Tipo": "Interfaz", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 30, "Descripción": "Problemas con el sistema de envío de correos masivos", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Sistema", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"}
]

# Crear DataFrame con los defectos
df_defectos = pd.DataFrame(defectos)

# Escribir en un nuevo archivo Excel
output_path = 'Registro_de_Defectos_Completado.xlsx'
df_defectos.to_excel(output_path, index=False)

print(f"Archivo generado: {output_path}")
'''
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# Crear un nuevo libro de trabajo y hojas
wb = Workbook()
ws_summary = wb.active
ws_summary.title = "Resumen"

# Información del caso de prueba
cases = [
    {"Número del Caso de Prueba": "CA001", "Componente": "CustomUser - Client", "Descripción de lo que se Probará": "Validar la creación de usuarios con diferentes roles y la asociación con clientes", "Prerrequisitos": "Sistema iniciado, sin usuarios existentes"},
    {"Número del Caso de Prueba": "CA002", "Componente": "Product", "Descripción de lo que se Probará": "Verificar la correcta creación y almacenamiento de productos", "Prerrequisitos": "Sistema iniciado, sin productos existentes"},
    {"Número del Caso de Prueba": "CA003", "Componente": "Order", "Descripción de lo que se Probará": "Comprobar el flujo de creación de pedidos y su estado", "Prerrequisitos": "Sistema iniciado, con productos y clientes existentes"},
    {"Número del Caso de Prueba": "CA004", "Componente": "Payment", "Descripción de lo que se Probará": "Validar el proceso de pago y actualización del estado de los pedidos", "Prerrequisitos": "Sistema iniciado, con pedidos pendientes"},
    {"Número del Caso de Prueba": "CA005", "Componente": "Delivery", "Descripción de lo que se Probará": "Verificar la gestión de entregas y actualización del estado de las mismas", "Prerrequisitos": "Sistema iniciado, con pedidos pagados y pendientes de entrega"},
    {"Número del Caso de Prueba": "CA006", "Componente": "SalesReport", "Descripción de lo que se Probará": "Validar la generación y almacenamiento de informes de ventas", "Prerrequisitos": "Sistema iniciado, con ventas registradas"}
]
# Crear DataFrame para el resumen del caso de prueba
df_summary = pd.DataFrame(cases)

# Añadir el resumen a la hoja de resumen
for r in dataframe_to_rows(df_summary, index=False, header=True):
    ws_summary.append(r)

# Información de los pasos del caso de prueba
steps = {
    "CA001": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un usuario con rol de Cliente", "Datos Entrada": "username, password, role=Cliente", "Salida Esperada": "Usuario creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Crear un usuario con rol de Administrador", "Datos Entrada": "username, password, role=Administrador", "Salida Esperada": "Usuario creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 3, "Descripción de pasos a seguir": "Asociar un cliente a un usuario", "Datos Entrada": "client user", "Salida Esperada": "Cliente asociado correctamente", "¿OK?": "", "Observaciones": ""}
    ],
    "CA002": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un producto con detalles completos", "Datos Entrada": "product_id, brand, name, price, stock, category", "Salida Esperada": "Producto creado y almacenado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Verificar que el producto se muestra en la lista de productos", "Datos Entrada": "N/A", "Salida Esperada": "Producto visible en la lista", "¿OK?": "", "Observaciones": ""}
    ],
    "CA003": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un pedido para un producto", "Datos Entrada": "product_id, quantity, client_name, client_address, client_email", "Salida Esperada": "Pedido creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Actualizar el estado del pedido a 'Approved'", "Datos Entrada": "order_id, status='Approved'", "Salida Esperada": "Estado del pedido actualizado", "¿OK?": "", "Observaciones": ""},
        {"Paso": 3, "Descripción de pasos a seguir": "Rechazar un pedido", "Datos Entrada": "order_id, status='Rejected'", "Salida Esperada": "Pedido rechazado correctamente", "¿OK?": "", "Observaciones": ""}
    ],
    "CA004": [
        {"Paso": 1, "Descripción de pasos a seguir": "Realizar un pago para un pedido aprobado", "Datos Entrada": "order_id, amount, payment_date", "Salida Esperada": "Pago realizado y registrado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Actualizar el estado del pago a 'Confirmed'", "Datos Entrada": "payment_id, status='Confirmed'", "Salida Esperada": "Estado del pago actualizado", "¿OK?": "", "Observaciones": ""}
    ],
    "CA005": [
        {"Paso": 1, "Descripción de pasos a seguir": "Registrar la entrega de un pedido pagado", "Datos Entrada": "order_id, delivery_date", "Salida Esperada": "Entrega registrada y estado actualizado", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Actualizar el estado de la entrega a 'Delivered'", "Datos Entrada": "delivery_id, status='Delivered'", "Salida Esperada": "Estado de la entrega actualizado", "¿OK?": "", "Observaciones": ""}
    ],
    "CA006": [
        {"Paso": 1, "Descripción de pasos a seguir": "Generar un informe de ventas para el mes actual", "Datos Entrada": "month", "Salida Esperada": "Informe de ventas generado y almacenado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Verificar los datos en el informe de ventas", "Datos Entrada": "N/A", "Salida Esperada": "Datos de ventas correctos y completos", "¿OK?": "", "Observaciones": ""}
    ]
}


# Añadir los pasos del caso de prueba a hojas individuales
for case_id, step_list in steps.items():
    ws_steps = wb.create_sheet(title=case_id)
    df_steps = pd.DataFrame(step_list)
    for r in dataframe_to_rows(df_steps, index=False, header=True):
        ws_steps.append(r)

# Guardar el archivo
wb.save("Pruebas de integracion 2.xlsx")


'''
cases = [
    {"Número del Caso de Prueba": "CA001", "Componente": "CustomUser - Client", "Descripción de lo que se Probará": "Validar la creación de usuarios con diferentes roles y la asociación con clientes", "Prerrequisitos": "Sistema iniciado, sin usuarios existentes"},
    {"Número del Caso de Prueba": "CA002", "Componente": "Product", "Descripción de lo que se Probará": "Verificar la correcta creación y almacenamiento de productos", "Prerrequisitos": "Sistema iniciado, sin productos existentes"},
    {"Número del Caso de Prueba": "CA003", "Componente": "Order", "Descripción de lo que se Probará": "Comprobar el flujo de creación de pedidos y su estado", "Prerrequisitos": "Sistema iniciado, con productos y clientes existentes"},
    {"Número del Caso de Prueba": "CA004", "Componente": "Payment", "Descripción de lo que se Probará": "Validar el proceso de pago y actualización del estado de los pedidos", "Prerrequisitos": "Sistema iniciado, con pedidos pendientes"},
    {"Número del Caso de Prueba": "CA005", "Componente": "Delivery", "Descripción de lo que se Probará": "Verificar la gestión de entregas y actualización del estado de las mismas", "Prerrequisitos": "Sistema iniciado, con pedidos pagados y pendientes de entrega"},
    {"Número del Caso de Prueba": "CA006", "Componente": "SalesReport", "Descripción de lo que se Probará": "Validar la generación y almacenamiento de informes de ventas", "Prerrequisitos": "Sistema iniciado, con ventas registradas"}
]

steps = {
    "CA001": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un usuario con rol de Cliente", "Datos Entrada": "username, password, role=Cliente", "Salida Esperada": "Usuario creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Crear un usuario con rol de Administrador", "Datos Entrada": "username, password, role=Administrador", "Salida Esperada": "Usuario creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 3, "Descripción de pasos a seguir": "Asociar un cliente a un usuario", "Datos Entrada": "client user", "Salida Esperada": "Cliente asociado correctamente", "¿OK?": "", "Observaciones": ""}
    ],
    "CA002": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un producto con detalles completos", "Datos Entrada": "product_id, brand, name, price, stock, category", "Salida Esperada": "Producto creado y almacenado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Verificar que el producto se muestra en la lista de productos", "Datos Entrada": "N/A", "Salida Esperada": "Producto visible en la lista", "¿OK?": "", "Observaciones": ""}
    ],
    "CA003": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un pedido para un producto", "Datos Entrada": "product_id, quantity, client_name, client_address, client_email", "Salida Esperada": "Pedido creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Actualizar el estado del pedido a 'Approved'", "Datos Entrada": "order_id, status='Approved'", "Salida Esperada": "Estado del pedido actualizado", "¿OK?": "", "Observaciones": ""},
        {"Paso": 3, "Descripción de pasos a seguir": "Rechazar un pedido",


cases = [
    {"Número del Caso de Prueba": "CA001", "Componente": "CustomUser - Client", "Descripción de lo que se Probará": "Validar la creación de usuarios con diferentes roles y la asociación con clientes", "Prerrequisitos": "Sistema iniciado, sin usuarios existentes"},
    {"Número del Caso de Prueba": "CA002", "Componente": "Product", "Descripción de lo que se Probará": "Verificar la correcta creación y almacenamiento de productos", "Prerrequisitos": "Sistema iniciado, sin productos existentes"},
    {"Número del Caso de Prueba": "CA003", "Componente": "Order", "Descripción de lo que se Probará": "Comprobar el flujo de creación de pedidos y su estado", "Prerrequisitos": "Sistema iniciado, con productos y clientes existentes"},
    {"Número del Caso de Prueba": "CA004", "Componente": "Payment", "Descripción de lo que se Probará": "Validar el proceso de pago y actualización del estado de los pedidos", "Prerrequisitos": "Sistema iniciado, con pedidos pendientes"},
    {"Número del Caso de Prueba": "CA005", "Componente": "Delivery", "Descripción de lo que se Probará": "Verificar la gestión de entregas y actualización del estado de las mismas", "Prerrequisitos": "Sistema iniciado, con pedidos pagados y pendientes de entrega"},
    {"Número del Caso de Prueba": "CA006", "Componente": "SalesReport", "Descripción de lo que se Probará": "Validar la generación y almacenamiento de informes de ventas", "Prerrequisitos": "Sistema iniciado, con ventas registradas"}
]

steps = {
    "CA001": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un usuario con rol de Cliente", "Datos Entrada": "username, password, role=Cliente", "Salida Esperada": "Usuario creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Crear un usuario con rol de Administrador", "Datos Entrada": "username, password, role=Administrador", "Salida Esperada": "Usuario creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 3, "Descripción de pasos a seguir": "Asociar un cliente a un usuario", "Datos Entrada": "client user", "Salida Esperada": "Cliente asociado correctamente", "¿OK?": "", "Observaciones": ""}
    ],
    "CA002": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un producto con detalles completos", "Datos Entrada": "product_id, brand, name, price, stock, category", "Salida Esperada": "Producto creado y almacenado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Verificar que el producto se muestra en la lista de productos", "Datos Entrada": "N/A", "Salida Esperada": "Producto visible en la lista", "¿OK?": "", "Observaciones": ""}
    ],
    "CA003": [
        {"Paso": 1, "Descripción de pasos a seguir": "Crear un pedido para un producto", "Datos Entrada": "product_id, quantity, client_name, client_address, client_email", "Salida Esperada": "Pedido creado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Actualizar el estado del pedido a 'Approved'", "Datos Entrada": "order_id, status='Approved'", "Salida Esperada": "Estado del pedido actualizado", "¿OK?": "", "Observaciones": ""},
        {"Paso": 3, "Descripción de pasos a seguir": "Rechazar un pedido", "Datos Entrada": "order_id, status='Rejected'", "Salida Esperada": "Pedido rechazado correctamente", "¿OK?": "", "Observaciones": ""}
    ],
    "CA004": [
        {"Paso": 1, "Descripción de pasos a seguir": "Realizar un pago para un pedido aprobado", "Datos Entrada": "order_id, amount, payment_date", "Salida Esperada": "Pago realizado y registrado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Actualizar el estado del pago a 'Confirmed'", "Datos Entrada": "payment_id, status='Confirmed'", "Salida Esperada": "Estado del pago actualizado", "¿OK?": "", "Observaciones": ""}
    ],
    "CA005": [
        {"Paso": 1, "Descripción de pasos a seguir": "Registrar la entrega de un pedido pagado", "Datos Entrada": "order_id, delivery_date", "Salida Esperada": "Entrega registrada y estado actualizado", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Actualizar el estado de la entrega a 'Delivered'", "Datos Entrada": "delivery_id, status='Delivered'", "Salida Esperada": "Estado de la entrega actualizado", "¿OK?": "", "Observaciones": ""}
    ],
    "CA006": [
        {"Paso": 1, "Descripción de pasos a seguir": "Generar un informe de ventas para el mes actual", "Datos Entrada": "month", "Salida Esperada": "Informe de ventas generado y almacenado correctamente", "¿OK?": "", "Observaciones": ""},
        {"Paso": 2, "Descripción de pasos a seguir": "Verificar los datos en el informe de ventas", "Datos Entrada": "N/A", "Salida Esperada": "Datos de ventas correctos y completos", "¿OK?": "", "Observaciones": ""}
    ]
}
'''