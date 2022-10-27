from math import prod
from clases.producto import Producto
from clases.pedido import Pedido

def menu():  
  print("""
------------------------ ORDENES DE COMPRAS ------------------------
\t Por favor ingrese una opcion:
\t 1. Agregar producto al carrito
\t 2. Eliminar producto del carrito
\t 3. Mostrar pedido
\t 4. Total del pedido
\t 5. Salir
""")

#CARRITO DE PRODUCTOS
carrito = Pedido()

#LISTA DE PRODUCTOS

p1 = Producto('Codido 1', "Leche", 123)
p2 = Producto('Codido 2', "Cafe", 325)
p3 = Producto('Codido 3', "Chicles", 80)
p4 = Producto('Codido 4', "Cereales", 214)
p5 = Producto('Codido 5', "Cerveza", 464)

listProductos = [p1, p2, p3, p4, p5]

def mostrar_productos():
  for j in listProductos:
    i = listProductos.index(j)
    print(listProductos[i])


def agregar_producto_carrito(nombreProd, cant):
  for prod in listProductos:
    i = listProductos.index(prod)
    if listProductos[i].nombreProducto == nombreProd: 
      carrito.agregar_producto(listProductos[i], cant)
    
def eliminar_producto_carrito(nombreP):
   for prod in listProductos:
    i = listProductos.index(prod)
    
    if listProductos[i].nombreProducto == nombreP: 
      carrito.eliminar_producto(listProductos[i])

opcion = -1
while opcion != '5':
    menu()
    opcion = input('Elija una opcion: ')

    if (opcion == '1'):
      mostrar_productos()

      prod = input('Ingrese el producto que desea agregar al carrito: ')
      cant = int(input('Ingrese cantidad de productos: '))
      
      agregar_producto_carrito(prod, cant)
       
    elif (opcion == '2'):
      print('PRODUCTOS DEL CARRITO\n')
      carrito.mostrar_pedido()

      p = input('Ingrese el producto que desea eliminar: ')
      eliminar_producto_carrito(p)
    
    elif (opcion == '3'):
      carrito.mostrar_pedido()

    elif (opcion == '4'):
      totalP = carrito.total_pedido()
      print('Total: ' + totalP)
    else:
      print('¡Gracias por visitar nuestra tienda!')   