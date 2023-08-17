"""
Inicializar un conjunto vacío y agregarle los valores de las siguiente variables
Restricción: Utilizar el metodo add
"""

numero_1 = 1
numero_2 = 2
numero_3 = 3

# COMPLETAR - INICIO
conjunto_vacio = set()
conjunto_vacio.add(numero_1)
conjunto_vacio.add(numero_2)
conjunto_vacio.add(numero_3)
print(conjunto_vacio)
# COMPLETAR - FIN

"""
Inicializar un conjunto vacío con los valores "5", "6" y "7" y agregarle los valores de
las siguiente variables
Restricción: Utilizar el metodo add
"""

nombre = "Esteban"
domicilio = "Los sauces 3446"
edad = "35"

# COMPLETAR - INICIO
conjunto_valores = {5, 6, 7}
conjunto_valores.add(nombre)
conjunto_valores.add(domicilio)
conjunto_valores.add(edad)
print(conjunto_valores)
# COMPLETAR - FIN

"""
Dados dos conjuntos calcular su interseccion utiilizando el caracter ampersand
"""

conjunto_03 = {1, 23, 4, 8, 5, 10, 15, 21}
conjunto_04 = {12, 4, 10, 21, 78}

# COMPLETAR - INICIO
interseccion = conjunto_03 & conjunto_04

print(interseccion)
# COMPLETAR - FIN

"""
Dados dos conjuntos calcular su union utiilizando el caracter pipe
"""

conjunto_05 = {1, 2, 3, 4}
conjunto_06 = {5, 6, 7, 8}

# COMPLETAR - INICIO
conjunto_union = conjunto_05 | conjunto_06
print(conjunto_union)
# COMPLETAR - FIN

"""
Dados dos conjuntos calcular su diferencia utiilizando el caracter menos
"""

conjunto_07 = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_08 = {2, 4, 6, 8}

# COMPLETAR - INICIO
diferencia = conjunto_07 - conjunto_08
print(diferencia)
# COMPLETAR - FIN

"""
Dados dos conjuntos calcular su diferencia utiilizando el metodo difference
"""

conjunto_07 = {1, 2, 3, 4, 5, 6, 7, 8}
conjunto_08 = {2, 4, 6, 8}

# COMPLETAR - INICIO
diferencia = conjunto_07.difference(conjunto_08)
print(diferencia)
# COMPLETAR - FIN

"""
Dados dos conjuntos calcular su diferencia diferencia simetrica utiilizando el caracter circunflejo
"""

conjunto_09 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_10 = {1, 2, 3, 5, 6, 7, 8}

# COMPLETAR - INICIO
diferencia_simetrica = conjunto_09 ^ conjunto_10
print(diferencia_simetrica)
# COMPLETAR - FIN

"""
Dados dos conjuntos calcular su diferencia diferencia simetrica utiilizando el metodo symmetric_difference
"""

conjunto_09 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
conjunto_10 = {1, 2, 3, 5, 6, 7, 8}

# COMPLETAR - INICIO
conjunto_diff_sim = conjunto_09.symmetric_difference(conjunto_10)
print(conjunto_diff_sim)
# COMPLETAR - FIN