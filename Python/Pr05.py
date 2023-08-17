"""
Formatear las siguientes variables de tipo string en un único string.
Restricción: Utilizar el operador +.
"""

variable_01 = "¡Buenos "
variable_02 = "días "
variable_03 = "a todos!"

# COMPLETAR - INICIO
str_variable = variable_01 + variable_02 + variable_03
print(" ", str_variable)
# COMPLETAR - FIN

"""
Formatear los siguientes strings en un único string.
Restricción: Usar directamente los strings y la concatenación automática (no
usar operadores).
"""

# "¡Mamá "
# "estoy concatenando "
# "strings!"

# COMPLETAR - INICIO
variable = str("¡Mama")
variable1 = str("estoy concatenando")
variable2 = str("strings!")
print(" ", variable, variable1, variable2)
# COMPLETAR - FIN

"""
Formatear las siguientes variables en un único string.
Aclaración: Se debe convertir la variable entera a string
Restricción: Utilizar el operador +.
"""

dvariable_01 = "Le debo "
fvariable_02 = 600
gvariable_03 = " pesos a un amigo."

# COMPLETAR - INICIO
frase1 = str("Le debo ")
numero = str(600)
frase2 = str(" pesos a un amigo.")
print(" ", frase1 + numero + frase2)
# COMPLETAR - FIN

"""
Formatear las siguientes variables en un único string.
Aclaración: No es necesario realizar conversiones de tipo.
Restricción: Utilizar el método format.
"""

variable_01 = "Le debo "
variable_02 = 6
variable_03 = " pesos a un amigo hace "
variable_04 = " años."
variable_05 = "Ezequiel"
# COMPLETAR - INICIO
variable_06 = 6
variable_07 = "Se llama "
strings_concatenados = f"{variable_01}{variable_02}{variable_03}{variable_06}{variable_04}{variable_07}{variable_05}"
print(strings_concatenados)
# COMPLETAR - FIN