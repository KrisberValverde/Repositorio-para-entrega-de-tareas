#Programa para ordenar la matriz

def ordenar_matriz(Numeros_impares):
    filas= len(Numeros_impares)
    columnas= len(Numeros_impares[0])
    lista= [elementos for fila in Numeros_impares for elementos in fila]
    lista.sort()
    Matriz_ordenada= [lista [i * columnas:(i+1) * columnas] for i in range(filas)]
    return Matriz_ordenada

#Matriz bidimensional 3x3
Numeros_impares= [[17,19,21],
                  [11,13,15],
                  [3,7,9],
                  ]

#Imprimir la matriz original
print ("La matriz original es:")
for fila in Numeros_impares:
    print(fila)

Matriz_ordenada= ordenar_matriz(Numeros_impares)

#Imprimir la matriz ordenada
print ("\nLa matriz ordenada de forma asendente es:")
for fila in Matriz_ordenada:
    print(fila)