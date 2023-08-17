"""Tome como parámetro una lista de números y devuelva el producto todos los números.
Si la lista está vacía debe devolver 0."""

def producto_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        producto = 1
        for num in lista:
            producto *= num
        return producto

lista_numeros = [1, 2, 3, 4]
resultado = producto_lista(lista_numeros)
print(resultado)

lista_vacia = []
resultado1 = producto_lista(lista_vacia)
print(resultado1)