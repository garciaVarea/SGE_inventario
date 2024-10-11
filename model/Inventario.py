import json

class Inventario:
    def __init__(self):
        self.inventario = {}

    def Mostrar(self):
        print("\nProductos disponibles: ")
        for producto, detalles in self.inventario.items():
            print(f"{producto}: ${detalles['precio']} (Cantidad: {detalles['cantidad']})")

    def OOS(self):
        print("\nProductos fuera de stock: ")
        for producto, detalles in self.inventario.items():
            if detalles["cantidad"] == 0:
                print(f"{producto} no tiene existencias.")

    def Venta(self):
        while True:
            inventario = Inventario()
            inventario.Mostrar()

            producto_vendido = input("\nIntroduce el nombre del producto que quieres comprar (o escribe 'salir' para volver al menú): ").lower()

            if producto_vendido == "salir":
                break

            if producto_vendido in self.inventario and self.inventario[producto_vendido]["cantidad"] > 0:
                cantidad_vendida = int(input(f"Introduce la cantidad de {producto_vendido} a comprar: "))

                if cantidad_vendida <= self.inventario[producto_vendido]["cantidad"]:
                    self.inventario[producto_vendido]["cantidad"] -= cantidad_vendida
                    print(f"Venta realizada: {cantidad_vendida} {producto_vendido}")
                    if self.inventario[producto_vendido]["cantidad"] == 0:
                        print(f"¡AVISO!: El producto {producto_vendido} se ha agotado y necesita reposición.")
                else:
                    print("Lo sentimos. No hay suficientes existencias de producto.")
            else:
                print("Producto no disponible o stock insuficiente.")

    def Actualizacion(self):
        with open("Inventario_actualizado.json", "w") as fichero_json:
            json.dump(self.inventario, fichero_json)

        print("\nInventario actualizado guardado con éxito en 'inventario_actualizado.json'.")