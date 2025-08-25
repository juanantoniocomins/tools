import tkinter as tk
from tkinter import ttk

def mostrar_opcion():
    seleccion = opcion_var.get()
    if seleccion == "Redes":
        texto.set("Has elegido la opción de redes.")
    elif seleccion == "Sistemas":
        texto.set("Has elegido la opción de sistemas.")
    elif seleccion == "Seguridad":
        texto.set("Has elegido la opción de seguridad.")
    else:
        texto.set("Selecciona una opción válida.")

# Crear ventana
root = tk.Tk()
root.title("Menú de Opciones")

# Bloquear maximizar
root.resizable(False, False)

# Calcular posición centrada
ancho, alto = 450, 180
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alto // 2) - (alto // 2)
root.geometry(f"{ancho}x{alto}+{x}+{y}")

# Variable de opción
opcion_var = tk.StringVar(value="Elige una opción")

# Frame superior para lista y botones
frame_superior = ttk.Frame(root)
frame_superior.pack(pady=20, padx=10, fill="x")

# Crear OptionMenu
opciones = ["Redes", "Sistemas", "Seguridad"]
menu = ttk.OptionMenu(frame_superior, opcion_var, opciones[0], *opciones)
menu.pack(side="left", padx=5)

# Botón mostrar
btn_mostrar = ttk.Button(frame_superior, text="Mostrar", command=mostrar_opcion)
btn_mostrar.pack(side="left", padx=5)

# Botón salir
btn_salir = ttk.Button(frame_superior, text="Salir", command=root.destroy)
btn_salir.pack(side="left", padx=5)

# Label para mostrar resultado
texto = tk.StringVar()
lbl = ttk.Label(root, textvariable=texto)
lbl.pack(pady=20)

root.mainloop()
