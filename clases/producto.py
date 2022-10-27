#Autor: Agostina Rodriguez
TIPO_DESC_FIJO = "Fijo"
TIPO_DESC_PORC = "Porcentaje"

class Descuento:
    
    def __init__(self, tipo, valor):

        if not isinstance(valor,int):
            raise ValueError('EL valor debe ser un numero')
        if not isinstance(tipo, str):
            raise ValueError('tipo debe ser un string')   
        if tipo != TIPO_DESC_PORC and tipo != TIPO_DESC_FIJO:
            raise ValueError('El tipo debe ser fijo o porcentaje')
        if tipo == TIPO_DESC_FIJO and valor <=0:
            raise ValueError('El valor en el tipo fijo debe ser mayor a 0')
        if tipo == TIPO_DESC_PORC and (valor<=0 or valor > 100):
            raise ValueError('El valor en el tipo de porcentake debe estar entre 1 u 100')

        self.__tipo = tipo
        self.__valor = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    def aplicar_descuento(self, precio):
        if self.__tipo == TIPO_DESC_FIJO:
            if precio > self.__valor:
                return precio - self.__valor
            else:
                return 0
        else:
            return precio - (precio * (self.__valor / 100))

class Producto:
    
    def __init__(self, codigo, nombreProducto, precio, descuento = None):
        self.__codigo = codigo
        self.__nombreProducto = nombreProducto
        self.__precio = precio 
        self.__descuento = descuento

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevoCodigo):
        self.__codigo = nuevoCodigo

    @property
    def nombreProducto(self):
        return self.__nombreProducto

    @nombreProducto.setter
    def nombreProducto(self, valor):
        self.__nombreProducto = valor

    @property
    def precio(self):
        if self.__descuento == None:
            return self.__precio
        else:
            return self.__descuento.aplicar_descuento(self.__precio)

    @precio.setter
    def precio(self, nuevoPrecio):
        self.__precio = nuevoPrecio

    @property
    def descuento(self):
        return self.__descuento

    @codigo.setter
    def descuento(self, descuento):
        self.__descuento = descuento


    def calcular_total(self, unidades):
        return self.precio * unidades

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombreProducto + ', precio: ' + str(self.__precio)

