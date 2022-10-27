from clases.producto import Producto

class Pedido():
    
    def __init__(self):
        self.__productos = []
        self.__cantidades = []

    def agregar_producto(self, producto, cantidad):

        if not isinstance(producto, Producto):
            raise Exception('el producto debe ser de la clase producto')

        if not isinstance(cantidad, int):
            raise Exception('cantidad debe ser un numero')

        if cantidad <= 0:
            raise Exception('cantidad debe ser mayor a 0')

        if producto in self.__productos:
            i = self.__productos.index(producto)
            self.__cantidades[i] += cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)    

    def eliminar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception('El producto debe ser la clase producto')

        if producto in self.__productos:
            i = self.__productos.index(producto)
            del self.__productos[i]
            del self.__cantidades[i]
        else:
            raise Exception('El producto no existe')

    def total_pedido(self):
        total = 0

    #Recorre dos lista a la vez
        for (p,c) in zip(self.__productos, self.__cantidades):
            total += p.calcular_total(c)

        return total

    def mostrar_pedido(self):
        for (p,c) in zip(self.__productos, self.__cantidades):
            print("Producto ->", p.nombreProducto, "cantidad: " + str(c))
        