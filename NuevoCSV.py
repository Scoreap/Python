import csv


# Solicitar datos
nombre = input("Nombre completo: ")
edad = input("Edad: ")
correo = input("Correo electrónico: ")

# Crear archivo CSV
with open("mi_datos.csv", "w", newline="") as archivo: # newline evita líneas en blanco extras en Windows.
    escritor = csv.writer(archivo)
    escritor.writerow(["Nombre", "Edad", "Correo"])  # Encabezados
    escritor.writerow([nombre, edad, correo])        # Datos

print("Archivo CSV creado con éxito.")

