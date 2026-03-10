class Cliente:
    def __init__(self, nombre, direccion, edad):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    def imprimirDetalles(self):
        print("Nombre del cliente:", self.nombre)
        print("Direccion:", self.direccion)
        print("Edad:", self.edad)