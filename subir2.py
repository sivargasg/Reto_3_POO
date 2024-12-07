class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calcular_precio_total(self):
        return self.price


class Bebida(MenuItem):
    def __init__(self, name: str, price: float, tamaño: str):
        super().__init__(name, price)
        self.tamaño = tamaño


class Aperitivo(MenuItem):
    def __init__(self, name: str, price: float, porción: str):
        super().__init__(name, price)
        self.porción = porción


class PlatoPrincipal(MenuItem):
    def __init__(self, name: str, price: float, acompañamientos: list):
        super().__init__(name, price)
        self.acompañamientos = acompañamientos


class Orden:
    def __init__(self):
        self.items = []

    def agregar_item(self, item: MenuItem):
        self.items.append(item)

    def calcular_total(self):
        return sum(item.calcular_precio_total() for item in self.items)

    def aplicar_descuento(self, porcentaje: float):
        total = self.calcular_total()
        return total * (1 - porcentaje / 100)


# Creación del menú con al menos 10 ítems
menu = [
    Bebida("Coca Cola", 1.5, "Mediana"),
    Bebida("Agua", 1.0, "Grande"),
    Aperitivo("Papas Fritas", 2.5, "Grande"),
    Aperitivo("Aros de Cebolla", 3.0, "Pequeña"),
    PlatoPrincipal("Hamburguesa", 5.0, ["Papas Fritas"]),
    PlatoPrincipal("Ensalada", 4.5, ["Pan"]),
    PlatoPrincipal("Pollo Asado", 6.0, ["Arroz", "Ensalada"]),
    Bebida("Jugo de Naranja", 2.0, "Mediana"),
    Aperitivo("Mozzarella Sticks", 3.5, "Mediana"),
    PlatoPrincipal("Pizza", 7.0, ["Salsa"])
]

# Ejemplo de uso
orden = Orden()
orden.agregar_item(menu[0])
orden.agregar_item(menu[4])
orden.agregar_item(menu[7])
print(f"Total sin descuento: {orden.calcular_total()}")
print(f"Total con descuento del 10%: {orden.aplicar_descuento(10)}")
