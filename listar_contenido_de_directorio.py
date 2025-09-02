# ------------------------------------------------------------
# Script: listar_directorio_tkinter.py
# Descripción: Selecciona un directorio, lista todos sus archivos
#              y subdirectorios, guarda la lista en un archivo TXT
#              y abre el archivo automáticamente.
#
# Requisitos:
# 1. Python 3.x
# 2. Tkinter (incluido en la mayoría de distribuciones de Python)
# ------------------------------------------------------------

import os
import tkinter as tk
from tkinter import filedialog
import subprocess  # Para abrir el archivo en Windows

# Función que selecciona el directorio y genera el listado
def listar_directorio():
    directorio = filedialog.askdirectory(title="Selecciona un directorio")
    if not directorio:
        return  # Si no se selecciona nada, salir
    
    # Crear lista con archivos y carpetas
    elementos = os.listdir(directorio)
    
    # Imprimir en consola
    print("Elementos encontrados:")
    for e in elementos:
        print(e)
    
    # Guardar en archivo txt
    ruta_txt = os.path.join(directorio, "listado.txt")
    with open(ruta_txt, "w", encoding="utf-8") as f:
        for e in elementos:
            f.write(e + "\n")
    
    # Abrir el archivo automáticamente (Windows)
    subprocess.Popen(['notepad.exe', ruta_txt])

# Crear ventana principal de Tkinter
root = tk.Tk()
root.title("Listado de Directorio")
root.geometry("300x100")

# Botón para seleccionar directorio y generar listado
btn = tk.Button(root, text="Seleccionar Directorio", command=listar_directorio)
btn.pack(expand=True)

root.mainloop()
