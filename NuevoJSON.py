import json

# Solicitar datos
nombre = input("Nombre completo: ")
edad = input("Edad: ")
correo = input("Correo electrónico: ")

# Crear un diccionario con los datos
datos = {
    "Nombre": nombre,
    "Edad": edad,
    "Correo": correo
}

# Crear archivo JSON
with open("mi_datos.json", "w") as archivo:
     #escribe el diccionario en el archivo JSON
     #indent: organiza el contenido para legilibilidad
    json.dump(datos, archivo, indent=4)

print("Archivo JSON creado con éxito.")
