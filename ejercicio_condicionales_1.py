"""

Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:

. 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
. 4 y 5                ---> Aprobado, la nota es ...
. 1, 2 y 3            ---> Desaprobado, la nota es ... 

"""

nota_aleatoria = int(input("Ingrese una nota: "))

if nota_aleatoria >= 6 and nota_aleatoria < 11:
    print (f"Su nota es {nota_aleatoria}, y promociona directamente.")
elif nota_aleatoria > 4 and nota_aleatoria < 6:
    print (f"Su nota es {nota_aleatoria} y está aprobada.")
elif nota_aleatoria < 3 and nota_aleatoria > 0:
    print (f"Su nota es {nota_aleatoria} y está desaprobada.")
else:
    print ("Error. Ingrese un número válido. Vuelva a ejecutar el programa.")
