#Diccionario que contiene información personal

Información_personal= {
    "Nombre": "Krisber Valverde",
    "Edad": 18,
    "Ciudad": "Shushufindi",
    "Profesión": "Estudiante",
}

# Acceso y modificación de la clave "Ciudad"
Información_personal["Ciudad"]= "Lago Agrio"

#Se agrega una nueva clave-valor "Profesión"
Información_personal["Profesión"]= "Lic. contabilidad"

# Verificamos si la clave "Teléfono" existe antes de agregarla
if "Teléfono" not in Información_personal:
    Información_personal["Teléfono"] = "0990213628"

# Agregar una nueva clave-valor ("Telefono" con mi número personal)
Información_personal["Teléfono"] = "0990213628"

# Eliminar la clave "Edad" del diccionario
del Información_personal["Edad"]

# Imprimir el diccionario final
print("Diccionario final:", Información_personal)