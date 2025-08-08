import time #para una impresion mas interesante en consola 
from pathlib import Path

# Crear ruta a escritorio
desktop = Path("D:/OneDrive - Universidad Rafael Landivar/Escritorio")
ruta = desktop / "1185324.txt"


#Ingreso de datos
print("---Bienvenido---\nIngrese los siguientes datos:\n")
nombreUsuario = input("Nombre: ")
carneUsuario = input("Carnet: ")
carreraUsuario = input("Carrera: ")
correoUsuario = input("Correo electronico: ")

#Crear y escribir archivo
with open(ruta, "w", encoding="utf-8") as archivo:
    archivo.write("D A T O S  P E R S O N A L E S\n")
    archivo.write("Nombre:  " + nombreUsuario + "\n")
    archivo.write("Carnet: " + carneUsuario + "\n")
    archivo.write("Carrera: " + carreraUsuario  + "\n")
    archivo.write("Correo electronico: " + correoUsuario + "\n")

    for punto in range(3):
        print(".", end=" ", flush=True)
        time.sleep(1)

    print("\nArchivo creado exitosamente.")