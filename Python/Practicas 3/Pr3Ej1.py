
from math import pi

class Circle:
    """Todo cículo tiene un radio y se desea conocer tanto el área como el
        perímetro (longitud de circunferencia).

        Reportar los números redondeados a dos decimales

        Restricciones:
            - Utilizar 1 variable de instancia
            - Utilizar 2 métodos de instancia
            - No utilizar variable de clase
            - No utilizar Dataclasses
            - No utilizar Properties
            - Utilizar Type Hints en todos los métodos y variables
        """


# NO MODIFICAR - INICIO
# Test básico
from math import pi

class Circle:
    def __init__(self, radio: float) -> None:
        self._radio = radio

    def area(self) -> float:
        return round(pi * self._radio ** 2, 2)

    def perimetro(self) -> float:
        return round(2 * pi * self._radio, 2)

circle = Circle(1)
print(circle._radio)
print(circle.area())
print(circle.perimetro())

circle = Circle(radio=1)
print(circle._radio)
print(circle.area())
print(circle.perimetro())

