class Cliente:
    def __init__(self, nombre, direccion, edad):
        # Guardamos los datos en los atributos del objeto
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad

    def imprimirDetalles(self):
        # Este método solo imprime la información
        print("\n--- Detalles del Cliente ---")
        print(f"Nombre: {self.nombre}")
        print(f"Dirección: {self.direccion}")
        print(f"Edad: {self.edad} años")
