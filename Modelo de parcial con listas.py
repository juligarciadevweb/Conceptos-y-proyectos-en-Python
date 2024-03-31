"""
	Enunciado:

Cargar un vector de N elementos que contengan las notas de un curso. Por medio de un menu
indicar:

b. Promedio de notas.
c. Cantidad de notas superiores al promedio.
d. Cantidad de alumnos aprobados y desaprobados. Se aprueba desde 6.

"""
n = int(input("Ingrese el numero de elementos del vector: "))
sup = 0 #notas superiores al promedio
ap = 0 #aprobados
dp = 0 #desaprobados
sum = 0
vec = []

for i in range(n):
    nota = int(input("Ingrese una nota: "))  # Se utiliza int(input()) para asegurar que la nota sea tratada como un número entero
    if nota > 0 and nota <= 10:
        vec.append(nota)  # Se agrega la nota a la lista vec utilizando el método append()
        if nota > 7:
            ap += 1
        else:
            dp += 1
        sum += nota
    else:
        nota = int(input("ERROR, ingrese la nota nuevamente: "))

prom = sum/n
print("Los desaprobados son: " + str(dp))
print("\nLos aprobados son "+ str(ap))
print("El promedio es: "+ str(prom))