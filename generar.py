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
