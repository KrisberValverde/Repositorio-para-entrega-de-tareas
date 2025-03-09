#Crear una matriz 3D con los datos de temperaturas diarias en varias ciudades

#Encontrar el promedio de temperaturas para cada ciudad y semana.

# Contenido de la primera dimensión: 3 ciudades
# Contenido de la segunda dimensión: 7 días de la semana
# Contenido de la tercera dimensión: 4 semanas

Matriz_de_Temperaturas = [
    [   # Lago Agrio
        [   # Semana N°1
            {"Día": "Lunes", "temperatura": 28},
            {"Día": "Martes", "temperatura": 27},
            {"Día": "Miércoles", "temperatura": 29},
            {"Día": "Jueves", "temperatura": 30},
            {"Día": "Viernes", "temperatura": 32},
            {"Día": "Sábado", "temperatura": 28},
            {"Día": "Domingo", "temperatura": 31}
        ],
        [   # Semana N°2
            {"Día": "Lunes", "temperatura": 33},
            {"Día": "Martes", "temperatura": 35},
            {"Día": "Miércoles", "temperatura": 34},
            {"Día": "Jueves", "temperatura": 29},
            {"Día": "Viernes", "temperatura": 27},
            {"Día": "Sábado", "temperatura": 30},
            {"Día": "Domingo", "temperatura": 31}
        ],
        [   # Semana N°3
            {"Día": "Lunes", "temperatura": 34},
            {"Día": "Martes", "temperatura": 35},
            {"Día": "Miércoles", "temperatura": 36},
            {"Día": "Jueves", "temperatura": 33},
            {"Día": "Viernes", "temperatura": 32},
            {"Día": "Sábado", "temperatura": 30},
            {"Día": "Domingo", "temperatura": 29}
        ],
        [   # Semana N°4
            {"Día": "Lunes", "temperatura": 28},
            {"Día": "Martes", "temperatura": 26},
            {"Día": "Miércoles", "temperatura": 25},
            {"Día": "Jueves", "temperatura": 28},
            {"Día": "Viernes", "temperatura": 30},
            {"Día": "Sábado", "temperatura": 32},
            {"Día": "Domingo", "temperatura": 29}
        ]
    ],
    [   # Shushufindi
        [   # Semana N°1
            {"Día": "Lunes", "temperatura": 30},
            {"Día": "Martes", "temperatura": 29},
            {"Día": "Miércoles", "temperatura": 27},
            {"Día": "Jueves", "temperatura": 28},
            {"Día": "Viernes", "temperatura": 29},
            {"Día": "Sábado", "temperatura": 30},
            {"Día": "Domingo", "temperatura": 32}
        ],
        [   # Semana N°2
            {"Día": "Lunes", "temperatura": 26},
            {"Día": "Martes", "temperatura": 28},
            {"Día": "Miércoles", "temperatura": 32},
            {"Día": "Jueves", "temperatura": 35},
            {"Día": "Viernes", "temperatura": 36},
            {"Día": "Sábado", "temperatura": 34},
            {"Día": "Domingo", "temperatura": 35}
        ],
        [   # Semana N°3
            {"Día": "Lunes", "temperatura": 33},
            {"Día": "Martes", "temperatura": 34},
            {"Día": "Miércoles", "temperatura": 35},
            {"Día": "Jueves", "temperatura": 32},
            {"Día": "Viernes", "temperatura": 30},
            {"Día": "Sábado", "temperatura": 29},
            {"Día": "Domingo", "temperatura": 30}
        ],
        [   # Semana N°4
            {"Día": "Lunes", "temperatura": 31},
            {"Día": "Martes", "temperatura": 33},
            {"Día": "Miércoles", "temperatura": 35},
            {"Día": "Jueves", "temperatura": 35},
            {"Día": "Viernes", "temperatura": 37},
            {"Día": "Sábado", "temperatura": 34},
            {"Día": "Domingo", "temperatura": 33}
        ]
    ],
    [   # Joya de los Sachas
        [   # Semana N°1
            {"Día": "Lunes", "temperatura": 29},
            {"Día": "Martes", "temperatura": 28},
            {"Día": "Miércoles", "temperatura": 30},
            {"Día": "Jueves", "temperatura": 31},
            {"Día": "Viernes", "temperatura": 29},
            {"Día": "Sábado", "temperatura": 32},
            {"Día": "Domingo", "temperatura": 33}
        ],
        [   # Semana N°2
            {"Día": "Lunes", "temperatura": 34},
            {"Día": "Martes", "temperatura": 36},
            {"Día": "Miércoles", "temperatura": 37},
            {"Día": "Jueves", "temperatura": 29},
            {"Día": "Viernes", "temperatura": 28},
            {"Día": "Sábado", "temperatura": 26},
            {"Día": "Domingo", "temperatura": 30}
        ],
        [   # Semana N°3
            {"Día": "Lunes", "temperatura": 29},
            {"Día": "Martes", "temperatura": 26},
            {"Día": "Miércoles", "temperatura": 28},
            {"Día": "Jueves", "temperatura": 27},
            {"Día": "Viernes", "temperatura": 29},
            {"Día": "Sábado", "temperatura": 32},
            {"Día": "Domingo", "temperatura": 30}
        ],
        [   # Semana N°4
            {"Día": "Lunes", "temperatura": 29},
            {"Día": "Martes", "temperatura": 27},
            {"Día": "Miércoles", "temperatura": 30},
            {"Día": "Jueves", "temperatura": 34},
            {"Día": "Viernes", "temperatura": 36},
            {"Día": "Sábado", "temperatura": 35},
            {"Día": "Domingo", "temperatura": 31}
        ]
    ]
]

# Cálculo del promedio de temperaturas para cada ciudad y semana

Ciudades = ["Lago Agrio", "Shushufindi", "Joya de los Sachas"]

for ciudad_idx, ciudad in enumerate(Matriz_de_Temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temperatura"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {Ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")