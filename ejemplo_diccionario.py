edades = {
    "Juan": 25,
    "María": 30,
    "Carlos": 28,
    "Ana": 22
}

# Imprimir un valor específico
print("La edad de Juan es:", edades["Juan"])

# Agregar un nuevo elemento
edades["Luis"] = 29

# Modificar un valor específico
edades["María"] = 31

# Eliminar un elemento específico
del edades["Carlos"]

# Verificar si existe un valor específico en el diccionario
if "Ana" in edades:
    print("Ana está en el diccionario.")

# Recorrer e imprimir todos los valores en el diccionario
for nombre, edad in edades.items():
    print(nombre, "tiene", edad, "años.")