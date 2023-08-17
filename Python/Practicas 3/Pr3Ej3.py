class Article:
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 property
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar métodos de instancia
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
    """

class Article:
    iva = 0.21

    def __init__(self, nombre: str, costo: float, descuento: float = 0) -> None:
        self._nombre = nombre
        self._costo = costo
        self._descuento = descuento

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def precio(self) -> float:
        precio_con_iva = self._costo + (self._costo * self.iva)
        precio_con_descuento = precio_con_iva - (precio_con_iva * self._descuento)
        return round(precio_con_descuento, 2)
    
article = Article("Auto", 1)
print(article.nombre)
print(article.precio)

article = Article("Auto", 1, 0.21)
print(article.nombre)
print(article.precio)

article = Article(costo=1, nombre="Auto")
print(article.nombre)
print(article.precio)
