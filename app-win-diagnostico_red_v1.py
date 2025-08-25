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
ancho, alto = 400, 200
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alto // 2) - (alto // 2)
root.geometry(f"{ancho}x{alto}+{x}+{y}")

# Variable de opción
opcion_var = tk.StringVar(value="Elige una opción")

# Crear OptionMenu
opciones = ["Redes", "Sistemas", "Seguridad"]
menu = ttk.OptionMenu(root, opcion_var, opciones[0], *opciones)
menu.pack(pady=20)

# Botón para mostrar texto
btn_mostrar = ttk.Button(root, text="Mostrar", command=mostrar_opcion)
btn_mostrar.pack(pady=5)

# Label para mostrar resultado
texto = tk.StringVar()
lbl = ttk.Label(root, textvariable=texto)
lbl.pack(pady=10)

# Botón de salir (abajo a la derecha)
frame_botones = ttk.Frame(root)
frame_botones.pack(fill="both", expand=True, padx=10, pady=10)
btn_salir = ttk.Button(frame_botones, text="Salir", command=root.destroy)
btn_salir.pack(side="right", anchor="se")

root.mainloop()
