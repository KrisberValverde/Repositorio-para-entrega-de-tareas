# Se escribe el archivo de texto

archivo= open ("my_notes.txt","w")

archivo.write("Mi nombre es Krisber Valverde \n")
archivo.write("Me gusta leer fantasia \n")
archivo.write("Me gustan las peliculas o series de policias \n")
archivo.write("Siempre trabajo mejor con musica \n")

#Cerramos los archivos
archivo.close()

# Leemos el archivo linea por linea
archivo= open ("my_notes.txt","r")
print("Contenido del archivo:")
linea= archivo.readline()
while linea:
    print(linea.strip())
    linea= archivo.readline()

#cerramos el archivo despues de la lectura
archivo.close()