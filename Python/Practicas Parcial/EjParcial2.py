"""Definir una función mayor(a,b,c) que reciba como parámetro 3 números y retorne el mayor."""
def mayor(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

resultado = mayor(1,4,6)
print(resultado)