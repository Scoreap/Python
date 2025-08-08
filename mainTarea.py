def crearArchivo():
    #crea el archivo y lo cierra automaticamente
    with open("practica2.txt", "w") as archivo:
        archivo.write("Actividad practica de la universidad")

def leerArchivo():
    archivoCreado = open('practica2.txt')
    contenido = archivoCreado.readlines() #da la opcion de agregar mas lineas
    for linea in contenido: #lee cada linea del archivo
        print("El archivo contiene: " + linea)
    archivoCreado.close()

#llama a las funciones
crearArchivo()
lecturaArchivo = leerArchivo()

print(lecturaArchivo)
