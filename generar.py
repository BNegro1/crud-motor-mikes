import pandas as pd

# Defectos identificados
defectos = [
    {"ID Defecto": 1, "Descripción": "El campo 'quantity' en el modelo 'Order' no tiene valor por defecto", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Datos", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 2, "Descripción": "La vista 'add_to_cart' no maneja correctamente la cantidad", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 3, "Descripción": "Filtro 'multiply' no registrado correctamente", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Interfaz", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 4, "Descripción": "Error 404 al agregar productos al carrito", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 5, "Descripción": "Productos no se muestran en la tienda", "Severidad": "Grave", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 6, "Descripción": "Errores de ruteo en URLs", "Severidad": "Medio", "Estado": "Corregido", "Tipo": "Sintaxis", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
    {"ID Defecto": 7, "Descripción": "Problemas en la autenticación y autorización", "Severidad": "Critico", "Estado": "Corregido", "Tipo": "Funcionalidad", "Fecha Reporte": "2024-07-06", "Fecha Resolución": "2024-07-06", "Responsable": "Desarrollador"},
]

# Crear DataFrame con los defectos
df_defectos = pd.DataFrame(defectos)

# Escribir en un nuevo archivo Excel
output_path = 'Registro_de_Defectos_Completado.xlsx'
df_defectos.to_excel(output_path, index=False)

print(f"Archivo generado: {output_path}")
