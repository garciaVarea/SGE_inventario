class Archivo:

    def __init__(self):
        self.inventario = {}

    def crear(self):
        ## Paso 1: crear el fichero de inventario
        with open("inventario.txt", "w") as fichero:
            productos = ["manzanas, 1.5, 10", "naranjas, 2.0, 5", "plátanos, 1.2, 20", "peras, 2.5, 0"]
            for producto in productos:
                fichero.write(producto + "\n")
        print("Fichero 'inventario.txt' creado con éxito")

    def leer(self):
        ## Paso 2: lee el fichero de texto e importa los datos a un diccionario; genera un aviso si hay productos sin stock
        inventario = {}
        with open("inventario.txt", "r") as fichero:
            for linea in fichero:
                nombre, precio, cantidad = linea.strip().split(",")
                self.inventario[nombre] = {"precio": float(precio), "cantidad": int(cantidad)}
        print("Inventario cargado desde 'inventario.txt': ")
        print(self.inventario, "\n")


