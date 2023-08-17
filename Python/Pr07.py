"""
A partir de ls siguiente lista instanciar una tupla que contenga todos sus valores
y en el mismo orden.
"""

lista = ["casa", "perro", "pato", "gato"]

# COMPLETAR - INICIO
tupla = tuple(lista)
print(tupla)
# COMPLETAR - FIN

"""
A partir de ls siguiente tupla instanciar una lista que contenga todos sus valores
y en el mismo orden.
"""

tupla = "casa", "perro", "pato", "gato", "tenedor"

# COMPLETAR - INICIO
lista = list(tupla)
print(lista)
# COMPLETAR - FIN

"""
Desempaquetar la siguiente tupla en las variables a, b y c
"""

tupla = ("primer", 25, [1, 2, 3])

# COMPLETAR - INICIO
a, b, c = tupla
print(a)
print(b)
print(c)
# COMPLETAR - FIN

"""
Desempaquetar la siguiente tupla y luego sumar sus valores
"""

tupla = (87, 98, 35, 67, 4, 9)

# COMPLETAR - INICIO
a, b, c, d, e, f = tupla
print(a + b + c + d + e + f)
# COMPLETAR - FIN

"""
Desempaquetar la siguiente lista y luego concatenar sus elementos
Restricción: Utilizar f-Strings.
"""

lista = ["esta", "mañana", "sali", "a", "correr"]

# COMPLETAR - INICIO
a, b, c, d, e = lista
mensaje = f"{a} {b} {c} {d} {e}"
print(mensaje)
# COMPLETAR - FIN

"""
Desempaquetar el primer elemento de la siguiente tupla
Restricción: Utilizar desempaquetado con comodines
"""

tupla = (73, 45, 344, 3434, 2)

# COMPLETAR - INICIO
a, *_ = tupla
primer_elemento = a
print(a)
# COMPLETAR - FIN

"""
Desempaquetar el primer y el último elemento de la siguiente lista y luego sumarlos
Restricción: Utilizar desempaquetado con comodines
"""

lista = [73, 45, 344, 3434, 2]

# COMPLETAR - INICIO
a, *_, b = lista
primer = a + b
print(primer)
# COMPLETAR - FIN

"""
Desempaquetar el primer, el segundo, el tercer, el cuarto y el quinto elemento de la
siguiente tupla y luego concatenarlos
Restricción: Utilizar desempaquetado con comodines y f-Strings
"""

tupla = ("anoche", "fui", "a", "la", "fiesta", "pero", "no", "pude", "entrar")

# COMPLETAR - INICIO
a, b, c, d, e, *_= tupla
concatenarlos = f"{a} {b} {c} {d} {e}"
print(concatenarlos)
# COMPLETAR - FIN