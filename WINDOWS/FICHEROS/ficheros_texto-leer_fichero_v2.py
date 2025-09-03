# ficheros_texto_gui_v2.py
# Compatible PyQt5 / PySide6
# Solo archivos .txt

# ficheros_texto_gui_v3.py
# Solo archivos .txt
import os

try:
    from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QFileDialog, QLabel
    from PyQt5.QtCore import Qt
    framework = "PyQt5"
except ImportError:
    from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout, QFileDialog, QLabel
    from PySide6.QtCore import Qt
    framework = "PySide6"

codificaciones = ['utf-8', 'utf-8-sig', 'cp1252', 'iso-8859-1', 'latin-1']

def abrir_fichero():
    """Abrir un fichero .txt y mostrar su contenido en el QTextEdit"""
    ruta, _ = QFileDialog.getOpenFileName(window, "Seleccionar fichero", "", "Archivos de texto (*.txt)")
    if not ruta:
        return  # No se seleccionó ningún archivo

    # Comprobar extensión
    if not ruta.lower().endswith(".txt"):
        label_estado.setText("Solo se pueden leer archivos .txt")
        area_texto.clear()
        return

    contenido = None
    for enc in codificaciones:
        try:
            with open(ruta, "r", encoding=enc) as f:
                contenido = f.read()
            label_estado.setText(f"Archivo leído correctamente con codificación: {enc}")
            break
        except UnicodeDecodeError:
            continue

    if contenido is None:
        label_estado.setText("No se pudo leer el archivo con las codificaciones probadas.")
        area_texto.clear()
    else:
        area_texto.setPlainText(contenido)

app = QApplication([])

# Ventana principal
window = QWidget()
window.setWindowTitle(f"Lector seguro de ficheros (.txt) ({framework})")
window.resize(600, 400)

# Centrar ventana
screen_geometry = app.primaryScreen().availableGeometry()
x = (screen_geometry.width() - window.width()) // 2
y = (screen_geometry.height() - window.height()) // 2
window.move(x, y)

# Layout principal
layout = QVBoxLayout()

# Etiqueta de estado
label_estado = QLabel("Selecciona un fichero .txt para leer")
label_estado.setAlignment(Qt.AlignCenter)
layout.addWidget(label_estado)

# Botón para abrir fichero
boton_abrir = QPushButton("Abrir fichero")
boton_abrir.clicked.connect(abrir_fichero)
layout.addWidget(boton_abrir, alignment=Qt.AlignCenter)

# Área de texto
area_texto = QTextEdit()
area_texto.setReadOnly(True)
layout.addWidget(area_texto)

# Asignar layout y mostrar ventana
window.setLayout(layout)
window.show()
app.exec()
