import json
import os

def MenuUsuarios():
    print("""
        --------------------------------
        -------- MENU USUARIOS ---------
        (1)Crear Usuario
        (2)Eliminar un Usuario
        (3)Lista de Usuario
          """)
    op = input("Ingrese Opcion Deseada --> ")
    match op:
        case "1":
            pass
        case "2":
            pass
        case "3":
            pass
###################################################################################
def guardarDatos(usuarios,nombre_archivo = 'usuarios.json'):
    with open(nombre_archivo,"a") as archivo:
        json.dump(usuarios, archivo, indent=4)

###################################################################################3
def cargarDatos(nombre_archivo='usuarios.json'):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return json.load(archivo)
    else:
        return []
    