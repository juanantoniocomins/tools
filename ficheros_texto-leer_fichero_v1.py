# ficheros_texto-leer_fichero_v2.py
# Versión: v2
# Requiere: Python 3.x
# Nota: Este script no necesita librerías externas para funcionar.
#       Intenta leer el fichero probando varias codificaciones comunes:
#       'utf-8', 'utf-8-sig', 'cp1252', 'iso-8859-1', 'latin-1'.
#       De esta forma, se evitan problemas con acentos y caracteres especiales.
#       Si se quisiera detectar automáticamente la codificación, se puede usar
#       la librería externa 'chardet' (instalable con: pip install chardet).

import os

# Cambiar al directorio del script
os.chdir(os.path.dirname(__file__))
print("Directorio actual:", os.getcwd())

codificaciones = ['utf-8', 'utf-8-sig', 'cp1252', 'iso-8859-1', 'latin-1']
contenido = None

for enc in codificaciones:
    try:
        with open("notas_alumnos.txt", "r", encoding=enc) as f:
            contenido = f.read()
        print(f"Archivo leído correctamente con codificación: {enc}")
        break
    except UnicodeDecodeError:
        continue

if contenido is None:
    print("No se pudo leer el archivo con las codificaciones probadas.")
else:
    print("\nContenido del archivo:\n")
    print(contenido)
