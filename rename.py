import os

# Directorio de origen (cambia esto a la ubicación de tu carpeta)
directorio_origen = './img2'

# Obtener una lista de todos los archivos en el directorio
archivos = os.listdir(directorio_origen)

# Ordenar la lista de archivos por nombre
archivos.sort()

# Contador para los nuevos nombres de archivo
contador = 14

# Recorre la lista de archivos y renómbralos
for archivo in archivos:
    # Construye el nuevo nombre de archivo
    nuevo_nombre = str(contador) + os.path.splitext(archivo)[1]
    
    # Ruta completa de los archivos originales y nuevos
    ruta_original = os.path.join(directorio_origen, archivo)
    ruta_nuevo = os.path.join(directorio_origen, nuevo_nombre)
    
    # Renombrar el archivo
    os.rename(ruta_original, ruta_nuevo)
    
    # Incrementar el contador
    contador += 1

print("Archivos renombrados exitosamente.")