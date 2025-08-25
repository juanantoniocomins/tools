import os

usuario = "juan"
carpeta = "C:/Users/" + usuario + "/Downloads"
for i, archivo in enumerate(os.listdir(carpeta), start=1):
    print(f"{archivo}")