#Programa para encontrar un valor de la matriz
#Matriz bidimensional 3x3

Numeros_pares= [[2,4,6],
                [8,10,12],
                [14,16,18]
                       ]

valor_a_encontrar = 10
for fila in range (len(Numeros_pares)):
    for columna in range (len(Numeros_pares[fila])):
        if Numeros_pares[fila][columna] == valor_a_encontrar:
            print(f"Ubicado en la fila {fila} "
                  f"y la columna {columna} "
                  f"el valor a encontrar es: {Numeros_pares[fila][columna]}")