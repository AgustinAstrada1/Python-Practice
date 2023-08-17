"""
Inicializar una lista vacía y luego agregarle 4 elementos cualquiera
Restricción: Utilizar el método append
"""

# COMPLETAR - INICIO
lista_01 = []
lista_01.extend([1, 2, 3])
lista_01.append(4)
len(lista_01)
print(" ", lista_01)
# COMPLETAR - FIN

"""
Extraer el cuarto elemento de la lista
Restricción: Utilizar el método pop
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO
elemento_extraido = lista.pop(3)
print(" ", elemento_extraido)
# COMPLETAR - FIN

"""
Concatenar las siguientes listas
Restricción: Utilizar el método extend
"""

lista_a = [1, 2, 3]
lista_b = ["4", "5", "6"]
lista_c = ["siete", "ocho", "nueve"]

# COMPLETAR - INICIO
lista_d = ["4", "5", "6", "siete", "ocho", "nueve"]
lista_a.extend(lista_d)
lista_contatenados_01 = lista_a
print(" ", lista_contatenados_01)
# COMPLETAR - FIN

"""
Agregar la variable variable_01 en la tercer posición de la lista lista_nueva
Restricción: Utilizar el método insert
"""

variable_01 = 2
lista_nueva = [0, 1, 3, 4]

# COMPLETAR - INICIO
lista_nueva.insert(2, variable_01)
print(" ", lista_nueva)
# COMPLETAR - FIN

"""
Armar una lista que contenga el primer y el último elemento de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, 42, 81, 6, "la"]

# COMPLETAR - INICIO
nueva_lista = [] 

nueva_lista.append(lista[0]) 
nueva_lista.append(lista[-1]) 

print(nueva_lista) 
# COMPLETAR - FIN

"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar el método append junto al indexado simple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
nueva_lista = [] 

nueva_lista.append(lista[0]) 
nueva_lista.append(lista[1]) 
nueva_lista.append(lista[2]) 

print(nueva_lista) 
# COMPLETAR - FIN

"""
Armar una lista que contenga los primeros 3 elementos de la siguiente lista
Restricción: Utilizar indexado múltiple
"""

lista = ["ho", 3.1416, "la", 81, 6, 42]

# COMPLETAR - INICIO
nueva_lista = lista[0:3]

print(nueva_lista)
# COMPLETAR - FIN

"""
Armar una lista que contenga los primeros 2 y los últimos 2 elementos de la
siguiente lista
Restricción: Utilizar el método extend junto al indexado múltiple
"""

lista = ["ho", "la", 81, 6, 42, "como", "estas?"]

# COMPLETAR - INICIO
nueva_lista = [] 

nueva_lista.extend(lista[0:2]) 
nueva_lista.extend(lista[-2:]) 

print(nueva_lista) 
# COMPLETAR - FIN

"""
Concatenar las siguientes 2 listas
Restricción: Utiliar el operador +
"""

lista_01 = [0, 1, 2, 3]
lista_02 = [5, 6]

# COMPLETAR - INICIO
nueva_lista = lista_01 + lista_02 

print(nueva_lista)
# COMPLETAR - FIN

"""
Concatenar 3 veces la siguiente lisa consigo misma
Restricción: Utiliar el operador *
"""

lista_01 = [0, 1, 0, 1, 0, 1]

# COMPLETAR - INICIO
nueva_lista = lista_01 * 3 

print(nueva_lista)
# COMPLETAR - FIN

"""
Verificar si el siguiente elemento pertenece a la lista
Restricción: Utiliar el operador in
"""

elemento = 1.0
lista = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1.0, 1, 0, 1, 0, 1]

# COMPLETAR - INICIO
if elemento in lista:
    print("El elemento", elemento, "pertenece a la lista")
else:
    print("El elemento", elemento, "no pertenece a la lista")
# COMPLETAR - FIN

"""
Verificar si las siguientes listas son iguales
Restricción: Utilizar el operador ==
"""

lista_01 = [1, 2, 3, 4.5, 6, 7]
lista_02 = [1, 3, 2, 4, 5, 6, 7]

# COMPLETAR - INICIO
if lista_01 == lista_02:
    print("Las listas son iguales")
else:
    print("Las listas son diferentes")
# COMPLETAR - FIN

"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno no tiene examenes aprobados.
Restricción: Utilizar el método any
"""

notas = [False, False, False, False, False, False, False, False, False]

# COMPLETAR - INICIO
if not any(notas):
    print("El alumno no tiene ningun examen aprobado")
else:
    print("El alumno tiene algun examen aprobado")
# COMPLETAR - FIN

"""
Se cuenta con una lista de elementos booleanos que corresponden a las notas de los exámenes
cuatrimestrales de un alumno (True si está aprobado y False en caso contrario)
Determinar si el alumno ha aprobado todos sus exámenes.
Restricción: Utilizar el método all
"""

notas = [True, True, False, True, True, True, True, True, True, True, True, True]

# COMPLETAR - INICIO
if all(notas):
    print("El alumno a aprobado todos sus examenes")
else:
    print("El alumno no ha aprobado todos sus examenes")
# COMPLETAR - FIN