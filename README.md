# Agentes_ARBA_Ret_Perc

Este script permite filtrar los archivos de texto del padrón de Agentes de Retención y Percepción ARBA basado en una lista de CUITs propia proporcionada en un archivo Excel.

## Requisitos

- Python 3.x
- Bibliotecas de Python: `pandas`, `tkinter`

## Uso

1. Ejecuta el script `Consulta txt ARBA vs xls Listado de clientes o proveedores - LS.py`.
2. Sigue los pasos en las ventanas emergentes para seleccionar el archivo Excel con los CUITs, el archivo .txt del padrón de ARBA, y dónde guardar el archivo de reporte.
3. El script procesará los archivos y generará un archivo de reporte con los resultados.

### Instrucciones Detalladas

1. **Seleccionar el archivo base de CUITs del sistema**:
   - El primer diálogo te pedirá seleccionar tu archivo Excel que contenga una columna denominada "CUIT", simplemente eso. Si tu archivo tiene una columna que cumpla esa condición... esa será la variable que el script compare entre el .xls y el .txt

2. **Seleccionar el archivo Per o Ret de ARBA**:
   - El segundo diálogo te va a pedir que selecciones el archivo de texto proviniente del padrón de ARBA.

3. **Seleccionar dónde guardar el archivo de reporte**:
   - El tercer diálogo te pedirá seleccionar una ubicación y un nombre para el archivo de reporte que se generará. Te recomiendo ser ordenadx desde el principio.

## Descripción del Script

El script realiza las siguientes acciones:

1. Abre una ventana para que el usuario seleccione un archivo Excel que contiene los CUITs.
2. Lee la columna "CUIT" del archivo Excel y prepara la lista de CUITs a buscar.
3. Abre una ventana para que el usuario seleccione un archivo .txt del padrón de ARBA.
4. Abre una ventana para que el usuario seleccione dónde guardar el archivo de reporte.
5. Lee el archivo de texto y ajusta los campos para preservar ceros a la izquierda. (Normalizar las entradas posibles para evitar omisiones)
6. Filtra las filas del archivo de texto que coinciden con los CUITs de la lista.
7. Guarda el resultado en el archivo de reporte. (Del paso 3 de las Instrucciones Detalladas)
8. Muestra el tiempo total de ejecución del script.

## Advertencias

- Asegúrate de que los archivos seleccionados sean correctos y contengan los datos necesarios.
- El script puede sobrescribir archivos existentes si no se selecciona un nombre único para el archivo de reporte.

