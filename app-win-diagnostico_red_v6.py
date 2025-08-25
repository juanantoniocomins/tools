import tkinter as tk
from tkinter import ttk

def mostrar_opcion():
    seleccion = opcion_var.get()
    if seleccion == "Redes":
        texto.set("Has elegido la opción de redes. Aquí podrás trabajar con sockets, escanear puertos, enviar pings, o crear pequeños servidores y clientes.")
    elif seleccion == "Sistemas":
        texto.set("Has elegido la opción de sistemas. Aquí podrás automatizar tareas, gestionar procesos, explorar el sistema de archivos y trabajar con variables de entorno.")
    elif seleccion == "Seguridad":
        texto.set("Has elegido la opción de seguridad. Aquí podrás probar hashing, cifrado, manejo de contraseñas y pequeños scripts de auditoría.")
    else:
        texto.set("Selecciona una opción válida.")

def resetear():
    texto.set("")

def copiar():
    root.clipboard_clear()
    root.clipboard_append(texto.get())
    root.update()  # mantiene el portapapeles aunque se cierre el programa

# Crear ventana
root = tk.Tk()
root.title("Menú de Opciones")
root.resizable(False, False)

# Dimensiones y centrado
ancho, alto = 900, 250   # << más ancho todavía
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alto // 2) - (alto // 2)
root.geometry(f"{ancho}x{alto}+{x}+{y}")

# Variable de opción
opcion_var = tk.StringVar(value="Elige una opción")

# Frame superior con lista + botones
frame_superior = ttk.Frame(root)
frame_superior.pack(pady=20)

# OptionMenu
opciones = ["Redes", "Sistemas", "Seguridad"]
menu = ttk.OptionMenu(frame_superior, opcion_var, opciones[0], *opciones)
menu.pack(side="left", padx=5)

# Botones
btn_mostrar = tk.Button(frame_superior, text="Mostrar", bg="green", fg="white", command=mostrar_opcion)
btn_mostrar.pack(side="left", padx=5)

btn_resetear = tk.Button(frame_superior, text="Resetear", bg="blue", fg="white", command=resetear)
btn_resetear.pack(side="left", padx=5)

btn_salir = tk.Button(frame_superior, text="Salir", bg="red", fg="white", command=root.destroy)
btn_salir.pack(side="left", padx=5)

btn_copiar = tk.Button(frame_superior, text="Copiar", bg="white", fg="black", command=copiar)
btn_copiar.pack(side="left", padx=5)

# Texto mostrado (Message en vez de Label)
texto = tk.StringVar()
lbl = tk.Message(root, textvariable=texto, width=800, anchor="center", justify="center")
lbl.pack(pady=20)

root.mainloop()
