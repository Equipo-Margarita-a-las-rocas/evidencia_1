edades=[]
num_edades=int(input('¿Cúantas edades quieres agregar?'))

for i in range (num_edades):
    edad=int(input('Ingresa la edad '+str(i+1)+': '))
    edades.append(edad)

for edad in edades:
    if edad >= 18:
        print(f'{edad} años: Usted es mayor de edad')
    else:
        print(f'{edad} años: Usted es menor de edad')

