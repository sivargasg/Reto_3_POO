class Punto:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y


class Linea:
    def __init__(self, inicio: Punto, fin: Punto):
        self.inicio = inicio
        self.fin = fin
        self.largo = self.sacar_largo()
        self.pendiente = self.sacar_pendiente()

    def sacar_largo(self):
        return ((self.fin.x - self.inicio.x) ** 2 + (self.fin.y - self.inicio.y) ** 2) ** 0.5

    def sacar_pendiente(self):
        if self.inicio.x == self.fin.x:
            return float('inf')
        return (self.fin.y - self.inicio.y) / (self.fin.x - self.inicio.x)

    def sacar_cruce_horizontal(self):
        if self.pendiente == 0:
            if self.inicio.x == 0:
                return float('inf')
            return None
        if self.inicio.y * self.fin.y > 0:
            return None
        cruce_x = self.inicio.x - (self.inicio.y / self.pendiente)
        return cruce_x

    def sacar_cruce_vertical(self):
        if self.pendiente == float('inf'):
            if self.inicio.x == 0:
                return float('inf')
            return None
        if self.inicio.x * self.fin.x > 0:
            return None
        cruce_y = self.inicio.y - (self.inicio.x * self.pendiente)
        return cruce_y

    def discretizar_linea(self, n):
        puntos = []
        dx = (self.fin.x - self.inicio.x) / n
        dy = (self.fin.y - self.inicio.y) / n
        for i in range(n + 1):
            puntos.append(Punto(self.inicio.x + i * dx, self.inicio.y + i * dy))
        return puntos


class Rectangulo:
    def __init__(self, linea1: Linea, linea2: Linea, linea3: Linea, linea4: Linea):
        self.linea1 = linea1
        self.linea2 = linea2
        self.linea3 = linea3
        self.linea4 = linea4

    def area(self):
        return self.linea1.sacar_largo() * self.linea2.sacar_largo()

    def perimetro(self):
        return 2 * (self.linea1.sacar_largo() + self.linea2.sacar_largo())

punto1 = Punto(x=0, y=5)
punto2 = Punto(x=3, y=-9)
linea1 = Linea(punto1, punto2)

