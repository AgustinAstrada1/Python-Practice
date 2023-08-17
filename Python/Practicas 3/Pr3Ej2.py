class Article:
    """Todos los artículos tienen un nombre y un costo, opcionalmente algunos
    tienen un porcentaje de descuento.

    El IVA es un impuesto que se aplica a todos los productos por igual,
    actualmente es de 21% pero puede cambiar en el futuro.

    Para calcular el precio de un artículo, hay que sumar el IVA y luego restar
    los descuentos si hubiera. Redondear a 2 decimales.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 método de instancia
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar Dataclasses
        - No utilizar Properties
        - Utilizar Type Hints en todos los métodos y variables
    """

class Article:
    iva = 0.21

    def __init__(self, nombre: str, costo: float, descuento: float = 0) -> None:
        self._nombre = nombre
        self._costo = costo
        self._descuento = descuento

    def precio(self) -> float:
        precio_con_iva = self._costo + (self._costo * self.iva)
        precio_final = precio_con_iva - (precio_con_iva * self._descuento)
        return round(precio_final, 2)

    @classmethod
    def actualizar_iva(cls, nuevo_iva: float) -> None:
        cls.iva = nuevo_iva

article = Article("Auto", 1)
print(article._nombre)
print(article.precio())

Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
print(article._nombre)
print(article.precio())