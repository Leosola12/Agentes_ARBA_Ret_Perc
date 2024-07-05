import pandas as pd
import tkinter as tk
from tkinter import filedialog
from time import time
from tkinter.messagebox import showinfo

root = tk.Tk()
root.withdraw()

# Inicio del proceso
Start = time()

# Seleccionar el archivo Excel
showinfo("Primer paso", "Seleccioná archivo base de CUITs del sistema")
excel_file = filedialog.askopenfilename()
df_excel = pd.read_excel(excel_file)

# Buscar la columna "CUIT"
cuits_a_buscar = df_excel["CUIT"].astype(str).str.replace(r'[\.-]', '').str.zfill(11).tolist() if "CUIT" in df_excel.columns else None
if cuits_a_buscar is None:
    print("No se encontró una columna con el rótulo 'CUIT'.")
    showinfo("ERROR", "No se encontró una columna con el rótulo 'CUIT'.")
    exit()

# Imprimir la lista de CUITs
print("Lista de CUITs a buscar:", cuits_a_buscar)

# Seleccionar el archivo de texto
showinfo("Segundo paso", "Seleccioná archivo Per o Ret de ARBA")
txt_file = filedialog.askopenfilename()

# Seleccionar dónde guardar el archivo de reporte
showinfo("Tercer paso", "Seleccionar dónde guardar el archivo de reporte, elegí un nombre para el archivo")
output_file = filedialog.asksaveasfilename(defaultextension=".txt", initialfile="Reporte de consulta al padrón v")

# Leer el archivo de texto con pandas
df_txt = pd.read_csv(txt_file, delimiter=';', header=None)

# Ajustar los campos específicos para preservar ceros a la izquierda
df_txt[1] = df_txt[1].apply(lambda x: str(x).zfill(8))  # Fecha de Publicación
df_txt[2] = df_txt[2].apply(lambda x: str(x).zfill(8))  # Fecha Desde
df_txt[3] = df_txt[3].apply(lambda x: str(x).zfill(8))  # Fecha Hasta
df_txt[9] = df_txt[9].apply(lambda x: str(x).zfill(2))  # Nro-Grupo

# Filtrar las filas que coinciden con los CUITs a buscar
df_resultado = df_txt[df_txt[4].astype(str).str.replace(r'[\.-]', '').str.zfill(11).isin(cuits_a_buscar)]

# Escribir el resultado en el archivo de reporte
df_resultado.to_csv(output_file, sep=';', header=False, index=False)

# Fin del proceso
End = time()

# Mostrar el tiempo de ejecución
showinfo("¡Listo! Fin del proceso", "El proceso ha finalizado en " + str(round(End - Start, 2)) + " segundos.")
