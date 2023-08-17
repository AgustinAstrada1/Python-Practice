lado_cuadrado = 5
area_cuadrado = pow(lado_cuadrado, 2)

# COMPLETAR - INICIO
area_mayor_a_cinco = not(lado_cuadrado == 5 and area_cuadrado <5)
# COMPLETAR - FIN
print("El area es: ", area_mayor_a_cinco)

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
True si el número 1 es divisible por 7 y al mismo tiempo el número 2 no lo es.
"""

numero_1 = 49
numero_2 = 50

# COMPLETAR - INICIO
resultado = not (numero_1 == 49%7 and numero_2 == 50%7)
# COMPLETAR - FIN
print("El resultado es: ", resultado)

"""
Construir una expresión lógica que use TODAS las variables y cuyo resultado sea
el mismo valor de la variable 3.
Restricción: sólo usar OR, NOT y el mecanismo de cortocircuito.
"""

variable_01 = False
variable_02 = True
variable_03 = 80
variable_04 = "90"
variable_05 = 100
# COMPLETAR - INICIO
resultado1 = (variable_01 and variable_03) or (not variable_01 and variable_02 and variable_03) or (variable_04 == str(variable_03) and variable_05 > variable_03)
# COMPLETAR - FIN
print("Resultado: ", resultado1)