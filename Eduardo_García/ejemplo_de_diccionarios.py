cedulas_prof = {
    "Dr. Pedro Limón": 963258741,
    "Dr. Karyme Mariel": 741258963,
    "Dr. Sergio Perez": 123987456,
}
print("La cedula profesional del Dr. Pedro Limón es:", cedulas_prof["Dr. Pedro Limón"])
cedulas_prof["Dr. Amy Garza"] = 1598753246
cedulas_prof["Dr. Karyme Mariel"] = 369852147
del cedulas_prof["Dr. Amy Garza"]
if "Dr. Pedro Limón" in cedulas_prof:
    print("El Dr. Pedro Limón se encuentra en la lista de cedulas.")
for nombre, edad in cedulas_prof.items():
    print("El", nombre, "tiene como cedula la siguiente: ", edad)