import tkinter as tk
from tkinter import ttk
import subprocess
import platform
import re

def mostrar_opcion():
    seleccion = opcion_var.get()
    
    if seleccion == "Ping a Google":
        sistema = platform.system()
        if sistema == "Windows":
            comando = ["ping", "8.8.8.8", "-n", "4"]
        else:
            comando = ["ping", "-c", "4", "8.8.8.8"]
        try:
            resultado = subprocess.run(comando, capture_output=True, text=True, timeout=10)
            salida = resultado.stdout
            mensaje = ""
            
            if sistema == "Windows":
                respuestas = re.findall(r"Respuesta desde .*: bytes=(\d+) tiempo=(\d+)ms TTL=(\d+)", salida)
                detalle_respuestas = ""
                for i, (bytes_val, tiempo, ttl) in enumerate(respuestas, 1):
                    detalle_respuestas += f" Paquete {i}: bytes={bytes_val} tiempo={tiempo}ms TTL={ttl}\n"
                
                match = re.search(r"Paquetes:\s*enviados\s*=\s*(\d+),\s*recibidos\s*=\s*(\d+),\s*perdidos\s*=\s*(\d+)", salida)
                if match:
                    enviados, recibidos, perdidos = match.groups()
                    porcentaje_match = re.search(r"\((\d+)%\s*perdidos\)", salida)
                    porcentaje = porcentaje_match.group(1) if porcentaje_match else "0"
                    mensaje = (
                        f"✅ Conectividad verificada. Internet funciona.\n\n"
                        f"Detalles de cada paquete:\n\n"
                        f"{detalle_respuestas}\n"
                        f"Resumen:\n\n"
                        f" Ping realizado a: 8.8.8.8\n"
                        f" Paquetes enviados: {enviados}\n"
                        f" Paquetes recibidos: {recibidos}\n"
                        f" Paquetes perdidos: {perdidos} ({porcentaje}%)"
                    )
                else:
                    mensaje = "⚠️ No se pudo analizar correctamente la salida del ping en Windows."
            else:
                respuestas = re.findall(r"(\d+) bytes from .*:.*time=(\d+\.?\d*) ms", salida)
                detalle_respuestas = ""
                for i, (bytes_val, tiempo) in enumerate(respuestas, 1):
                    detalle_respuestas += f" Paquete {i}: bytes={bytes_val} tiempo={tiempo} ms\n"
                
                match = re.search(r"(\d+) packets transmitted, (\d+) received, (\d+)% packet loss", salida)
                if not match:
                    match = re.search(r"(\d+) paquetes transmitidos, (\d+) recibidos, (\d+)% pérdida", salida)
                
                if match:
                    enviados, recibidos, porcentaje = match.groups()
                    mensaje = (
                        f"✅ Conectividad verificada. Internet funciona.\n\n"
                        f"Detalles de cada paquete:\n\n"
                        f"{detalle_respuestas}\n"
                        f"Resumen:\n\n"
                        f" Ping realizado a: 8.8.8.8\n"
                        f" Paquetes enviados: {enviados}\n"
                        f" Paquetes recibidos: {recibidos}\n"
                        f" Paquetes perdidos: {porcentaje}%\n"
                    )
                else:
                    mensaje = "⚠️ No se pudo analizar correctamente la salida del ping en Linux/Mac."
            
            texto.set(mensaje)
        except Exception as e:
            texto.set(f"Error al hacer ping: {e}")
    
    elif seleccion == "Interfaz de Red":
        try:
            salida = subprocess.check_output("ipconfig /all", shell=True)
            salida = salida.decode("cp850", errors="replace")  # Evita errores de acentos
            adaptadores = salida.split("\n\n")
            mensaje = ""

            # Nombre del host multiplataforma
            import socket
            nombre_host = socket.gethostname()
            mensaje += f"=== Nombre de Host: {nombre_host} ===\n\n"

            for bloque in adaptadores:
                if "Adaptador de Ethernet" in bloque:
                    lineas = bloque.splitlines()
                    nombre = lineas[0].strip()
                    descripcion = ""
                    for linea in lineas:
                        if "Descripción" in linea:
                            descripcion = linea.split(":", 1)[1].strip()
                            break
                    mensaje += f"\n=== {nombre} ({descripcion}) ===\n"

                    # IPv4
                    ipv4 = re.search(r"Dirección IPv4.*: ([\d\.]+)", bloque)
                    if ipv4:
                        mensaje += f"IPv4: {ipv4.group(1)}\n"

                    # Máscara de subred
                    mascara = re.search(r"Máscara de subred.*: ([\d\.]+)", bloque)
                    if mascara:
                        mensaje += f"Máscara: {mascara.group(1)}\n"

                    # Puerta de enlace
                    puerta = re.search(r"Puerta de enlace predeterminada.*: ([\d\.]+)", bloque)
                    if puerta:
                        mensaje += f"Puerta de enlace: {puerta.group(1)}\n"

                    # MAC
                    mac = re.search(r"Dirección física.*: ([\w-]+)", bloque)
                    if mac:
                        mac_formateada = mac.group(1).replace("-", ":")
                        mensaje += f"MAC: {mac_formateada}\n"

                    # DNS en la misma línea
                    dns = re.findall(r"Servidores DNS.*: ([\d\.]+)", bloque)
                    if dns:
                        mensaje += "DNS: " + ", ".join(dns) + "\n"

            texto.set(mensaje if mensaje else "⚠️ No se encontraron adaptadores Ethernet.")
        except Exception as e:
            texto.set(f"Error al obtener información de red: {e}")
    
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
    root.update()

# Crear ventana
root = tk.Tk()
root.title("Menú de Opciones")
root.resizable(False, False)

# Dimensiones y centrado
ancho, alto = 800, 450
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho // 2)
y = (pantalla_alto // 2) - (alto // 2)
root.geometry(f"{ancho}x{alto}+{x}+{y}")

# Variables
opcion_var = tk.StringVar(value="Elige una opción")
texto = tk.StringVar()

# Frame superior con lista + botones
frame_superior = ttk.Frame(root)
frame_superior.pack(pady=20)

# OptionMenu
opciones = ["Ping a Google", "Sistemas", "Seguridad", "Interfaz de Red"]
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
lbl = tk.Message(root, textvariable=texto, width=800, anchor="center", justify="left")
lbl.pack(pady=20)

root.mainloop()
