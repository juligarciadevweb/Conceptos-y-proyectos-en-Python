					###Diccionarios###
"""
Son los mapas en algunos lenguajes.estructura de datos que permite almacenar cualquier tipo de información, desde cadenas de texto o 
caracteres hasta números enteros, con decimales, listas e incluso otros diccionarios
"""

# Definición

my_first_dict = dict()
my_only_dict = {} #Lo puedo definir de las 2 maneras

print(type(my_first_dict))
print(type(my_only_dict))

my_cv_dict = {"Name": "JuliDev",
                 "Surname": "Frias", 
                 "Age": 20, 
                 "Lenguaje": "Rust",
                 "Collegue": "UTN-FRT",
                 2 : "ingenieria"}
    #Estamos agrupando y organizando los datos con una relacion clave-valor
    	#Clave ---> "Name": "JuliDev" <--- Valor

print(my_cv_dict)

my_dic_set = {"Name" : "Juan",
			  "Surname" : "Gomez",
			  "Age" : 23,
			  "Company": "Globant", # Acordate siempre de poner las ,
			  "Studies":{ #Tenemos un set dentro de un diccionario
			  		"Tecnico en electronica",
			  		"Ingenieria en sistemas",
			  		"Tecnico en programacion"
			  	}
			}

print(len(my_dic_set)) #Output: 5 porque cuenta las relaciones clave - valor			
print(my_dic_set)

#Impresion por clave-valor
print(my_dic_set["Surname"]) # Accede a la clave "surname" = Gomez
print(my_dic_set["Age"]) # Accede a la edad "Age" = 23
print(my_dic_set["Studies"]) #Accede al campo studies = {'Tecnico en electronica', 'Ingenieria en sistemas', 'Tecnico en programacion'}
print(my_cv_dict[2]) # Accede al campo 2 de my_cv_dic = ingenieria

#Inserción y reemplazo de valores
my_dic_set["Company"] = "Coca cola" #Reemplazo el valor de "Company"
print(my_dic_set["Company"]) # Output = Coca cola
my_dic_set["Age"] = 16
print(my_dic_set["Age"]) #Age de 23 a 16

#Eliminacion de datos
del my_dic_set["Age"]
print(my_dic_set)
"""
{'Name': 'Juan', 'Surname': 'Gomez', 'Company': 'Coca cola', 'Studies': 
{'Tecnico en programacion', 'Ingenieria en sistemas', 'Tecnico en electronica'}}
"""

print("Julian" in my_dic_set) # Output false porque busca por clave 
print("Surname" in my_dic_set) # Output true porque busca por clave

print(my_dic_set.items())
"""
dict_items([('Name', 'Juan'), ('Surname', 'Gomez'), ('Company', 'Coca cola'), 
('Studies', {'Tecnico en programacion', 'Tecnico en electronica', 'Ingenieria en sistemas'})])
"""

print(my_dic_set.keys()) #output = dict_keys(['Name', 'Surname', 'Company', 'Studies'])
print(my_dic_set.values()) #output = dict_values(['Juan', 'Gomez', 'Coca cola', {'Ingenieria en sistemas', 'Tecnico en electronica', 'Tecnico en programacion'}]) 

#Creacion de un diccionario nuevo que no tiene valores
my_new_fromk = dict.fromkeys(("Nombre", 1, "Piso"))
print((my_new_fromk)) #{'Nombre': None, 1: None, 'Piso': None}


