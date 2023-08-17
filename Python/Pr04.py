"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
int_numero_01 = int(123)
int_numero_02 = int(456)
int_numero_03 = int(789)
int_numero_04 = int(132)
suma_de_enteros = int_numero_01 + int_numero_02 + int_numero_03 + int_numero_04
print("La suma de los numeros es: ", suma_de_enteros)
# COMPLETAR - FIN

"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
str_numero_01 = str(123)
str_numero_02 = str(456)
str_numero_03 = str(789)
suma_de_numeros_string = str_numero_01 + str_numero_02 + str_numero_03
print("Numeros de enteros a string: ", suma_de_numeros_string)
# COMPLETAR - FIN

"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO
int_numero_binario = int(0b111010110101110111101000000)
int_numero_octal = int(0o1425)
int_numero_hexadecimal = int(0x6f540)
multiplicacion = int_numero_binario * int_numero_octal * int_numero_hexadecimal
print("La multiplicacion da como resultado: ", multiplicacion)
# COMPLETAR - FIN

"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO
n_numero_01 = int(987)
n_numero_02 = int(0x6f54F)
n_numero_03 = int(0o1234)
n_numero_04 = int(654)
resta = n_numero_01 - n_numero_02 - n_numero_03 - n_numero_04
print("El resultado de la resta es: ", resta)
# COMPLETAR - FIN