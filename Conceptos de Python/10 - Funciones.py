				#Funciones

#Todo lo que tengamos tabulado hacia la derecha va a pertenecer a esa funcion
def my_first_fun(): 
	print("Vamos bien")

my_first_fun()
my_first_fun()

num1 = 2 #Argumentos de la funcion
num2 = 7

def sum_two_values(num2, num1):
	suma = num2 + num1
	print(suma)

sum_two_values(num2, num1)

# Función con parámetros de entrada/argumentos por clave

def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Moure", name="Brais") #Le doy los argumentos por clave

# Función con parámetros de entrada/argumentos arbitrarios

def print_upper_texts(*texts): #Parametro de cadenas de caracteres
    print(type(texts)) #Output = <class 'tuple'>
    for text in texts: 
        print(text.upper()) #Imprime el texto en mayusculas como una tupla

print_upper_texts("Hola", "Rust", "JuliDev")
print_upper_texts("Finish")

# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias):
    print(f"{name} {surname} {alias}")

    #Llamadas
print_name_with_default("Darren", "Chris", "Colfer")
print_name_with_default("Claire", "Soledad", "Stella")

