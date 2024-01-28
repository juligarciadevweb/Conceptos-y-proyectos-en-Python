					#Sets
"""
Estructura de datos usada para almacenar elementos de 
una manera similar a las listas, pero con ciertas diferencias.

Los elementos de un set son únicos, no puede haber elementos duplicados.
Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados.
Sus elementos deben ser inmutables.

"""

#Definicion
my_initial_set = set()
my_other_set = {}

print(type(my_initial_set))
print(type(my_other_set))  # Inicialmente es un diccionario

my_initial_set = {"Juan", "JuliDev", "Nicolas", 35, "Rafael", 8.666}
print(type(my_initial_set)) #output: <class 'dict'>

print(len(my_initial_set)) # Nos dira el numero de elementos que tiene el set

#Agregando datos

my_initial_set.add("Sol") 

print(my_initial_set)  # Un set no es una estructura ordenada

my_initial_set.add("Sol")  # Un set NO admite elementos repetidos
# El elemento "Sol" no se agregara porque ya fue insertado anteriormente
print(my_initial_set)

#Busqueda
print("JuliDev" in my_initial_set) # Output: true
print("Lopez" in my_initial_set) # Output: false
print("Francisco" in my_initial_set)
my_initial_set.add("Francisco") # Agregamos francisco al set
print("Francisco" in my_initial_set) # Output: true

#Eliminacion unica
my_initial_set.remove("JuliDev") # Output: {'Nicolas', 35, 'Sol', 'Rafael', 8.666, 'Juan', 'Francisco'}
print(my_initial_set)
			#Eliminacion parcial
mi_set = {1, 1142, 0.523, 448, 45875}
print("Conjunto original:", mi_set)

# Usando el método clear para eliminar todos los elementos
mi_set.clear() #Vacia los elementos del set pero el mismo sigue creado

print("Conjunto después de clear:", mi_set)
"""Output: Conjunto después de clear: set()
La representación set() indica que el 
conjunto está vacío después de aplicar el método clear().
"""

			#Eliminacion total
del mi_set
#print(mi_set) #Output: NameError: name 'mi_set' is not defined

# Transformación

my_set = {"Pablo", "Jg", 35, "Ricardo", "Alberto Fernandez"}
my_list = list(my_set) # Transformo el set en una lista
print(my_list)
print(my_list[3]) # Ricardo

my_other_set = {"Kotlin", "Swift", "Python"}

# Otras operaciones - Union

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Programacion", "Laboratorio"}))
print(my_new_set.difference(my_set))
