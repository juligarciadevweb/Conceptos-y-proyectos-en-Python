"""
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
"""
word_one = input("Ingrese la primera palabra: ")
word_two = input("Ingrese la primera palabra: ")

def is_Anagrama(word_one, word_two):
	if word_one.lower() == word_two.lower():
		return false
	return sorted(word_one.lower) == sorted(word_two.lower) 

print(is_Anagrama(word_one, word_two))