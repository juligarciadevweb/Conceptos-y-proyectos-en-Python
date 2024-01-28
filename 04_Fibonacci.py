"""
* Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
"""

def Fibonacci():
	
	prev = 0
	next = 1

	for index in range(0,51):
		print(prev)
		 
		fib = prev + next
		prev = next
		next = fib

Fibonacci()