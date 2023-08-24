edad = int(input("Por favor ingresa tu edad a continuación: "))
nombre = input("Por favor ingresa tu nombre a continuación: ")  
persona = (nombre, edad)  

if edad >= 18:
    print("Usted es mayor de edad")
else:
    print("Usted aún es menor de edad")

txt_fin= f"{nombre} tiene {edad} años"
print (txt_fin)