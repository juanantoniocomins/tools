"""
Programa: Reductor de JPEG con interfaz gráfica (Tkinter)

Descripción:
Este programa permite seleccionar una imagen JPEG, reducir su tamaño mediante compresión
y/o ajuste de resolución, y guardar la versión reducida en otra ubicación. 
Al seleccionar la imagen original, el campo de destino se rellena automáticamente con
el mismo nombre pero añadiendo 'nuevo' al final.

Cómo usarlo:
1. Haz clic en "Seleccionar" para elegir la imagen JPEG que deseas reducir.
2. Opcionalmente, ajusta:
   - Calidad (1-100): mayor valor = mejor calidad, menor compresión.
   - Ancho máximo / Alto máximo: limita la resolución de la imagen.
3. Haz clic en "Reducir Imagen" para crear la versión reducida.
4. La imagen reducida se guardará en la ruta indicada en "Archivo destino".
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def reducir_tamano_jpeg(ruta_origen, ruta_destino, calidad=50, max_ancho=None, max_alto=None):
    imagen = Image.open(ruta_origen)
    
    # Redimensionar si se proporciona ancho o alto máximo
    if max_ancho or max_alto:
        ancho, alto = imagen.size
        if max_ancho and ancho > max_ancho:
            alto = int((max_ancho / ancho) * alto)
            ancho = max_ancho
        if max_alto and alto > max_alto:
            ancho = int((max_alto / alto) * ancho)
            alto = max_alto
        imagen = imagen.resize((ancho, alto), Image.ANTIALIAS)
    
    # Guardar la imagen reducida
    imagen.save(ruta_destino, "JPEG", quality=calidad)

def seleccionar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if archivo:
        entry_origen.delete(0, tk.END)
        entry_origen.insert(0, archivo)
        
        # Crear ruta destino automáticamente con "_nuevo" antes de la extensión
        carpeta, nombre = os.path.split(archivo)
        nombre_base, ext = os.path.splitext(nombre)
        archivo_destino = os.path.join(carpeta, f"{nombre_base}_nuevo{ext}")
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, archivo_destino)

def guardar_archivo():
    archivo = filedialog.asksaveasfilename(defaultextension=".jpg",
                                           filetypes=[("JPEG files", "*.jpg;*.jpeg")])
    if archivo:
        entry_destino.delete(0, tk.END)
        entry_destino.insert(0, archivo)

def reducir():
    origen = entry_origen.get()
    destino = entry_destino.get()
    try:
        calidad = int(entry_calidad.get())
        max_ancho = int(entry_ancho.get()) if entry_ancho.get() else None
        max_alto = int(entry_alto.get()) if entry_alto.get() else None
        reducir_tamano_jpeg(origen, destino, calidad=calidad, max_ancho=max_ancho, max_alto=max_alto)
        messagebox.showinfo("Éxito", f"Imagen reducida correctamente:\n{destino}")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo reducir la imagen:\n{e}")

# Crear ventana
root = tk.Tk()
root.title("Reductor de JPEG")

tk.Label(root, text="Archivo origen:").grid(row=0, column=0, sticky="e")
entry_origen = tk.Entry(root, width=50)
entry_origen.grid(row=0, column=1)
tk.Button(root, text="Seleccionar", command=seleccionar_archivo).grid(row=0, column=2)

tk.Label(root, text="Archivo destino:").grid(row=1, column=0, sticky="e")
entry_destino = tk.Entry(root, width=50)
entry_destino.grid(row=1, column=1)
tk.Button(root, text="Guardar como", command=guardar_archivo).grid(row=1, column=2)

tk.Label(root, text="Calidad (1-100):").grid(row=2, column=0, sticky="e")
entry_calidad = tk.Entry(root)
entry_calidad.insert(0, "50")
entry_calidad.grid(row=2, column=1, sticky="w")

tk.Label(root, text="Ancho máximo:").grid(row=3, column=0, sticky="e")
entry_ancho = tk.Entry(root)
entry_ancho.grid(row=3, column=1, sticky="w")

tk.Label(root, text="Alto máximo:").grid(row=4, column=0, sticky="e")
entry_alto = tk.Entry(root)
entry_alto.grid(row=4, column=1, sticky="w")

tk.Button(root, text="Reducir Imagen", command=reducir).grid(row=5, column=1, pady=10)

root.mainloop()
