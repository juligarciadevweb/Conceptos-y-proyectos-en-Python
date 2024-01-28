					#Variables
my_string_variable = "My String variable"
my_int_variable = 5
print(my_int_variable)

# Convertimos de tipo entero a string
my_int_to_str = str(my_int_variable) # Usamos la reasignacion
print(my_int_to_str)
print(type(my_int_to_str)) #<class 'str'>

my_bool_variable = False 
print(my_bool_variable) # False

# Concatenación de variables en un print
print(my_string_variable, my_int_to_str, my_bool_variable) # output: My String variable 5 False
print("Este es el valor de: ", my_bool_variable) # output: Este es el valor de:  False

# Algunas funciones del sistema
print(len(my_string_variable)) # Output: 18
# el len nos dira la cantidad de caracteres de la cadena, incluidos los espacios en blanco

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "Moure", 'MoureDev', 35
print("Me llamo:", name, surname, ". Mi edad es:",
      age, ". Y mi alias es:", alias)

# Entradas de datos por variables

name = input('Nombre: ')
age = input('Edad: ')
print(name)
print(age)

# Cambio de tipo
name_creator = 50
age = "JuliDev"
print(name_creator)
print(age)
