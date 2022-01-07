
import random
import time

bodega=[] 

def main():
    """
    Inicio del programa de bodega
    ---
    Se llena lista con 3 valores de diccionario con un stock inicial entre 300 y 500
    """
    stock=random.randint(300,500)
    bodega.append(
        {"ID":1,"Nombre":"Vasos","Stock":stock})
    stock=random.randint(300,500)
    bodega.append(
        {"ID":2,"Nombre":"Cuchara","Stock":stock})
    stock=random.randint(300,500)
    bodega.append(
        {"ID":3,"Nombre":"Tenedor","Stock":stock})
    print("Sistema de bodega")
    

def sumar_Y_disminuirCantPro(idPro,cant,accion):
    """
        Funcion agregar y quitar stock
        --
        se busca producto segun id del parametro con su cantidad correspondiente
        la accion define si va a sumar o quitar
        ej. 1=sumar y 2 = quitar
    """
    for i in bodega:
        if i["ID"]==idPro:
            
            if accion==1: #sumar
                i["Stock"]+=int(cant)
            elif accion==2: #quitar
                i["Stock"]-=int(cant)
        
def agregarProducto(idPro,nombre):
    """
    Agregar producto
    --
    funcion para agregar un nuevo producto ingresando id y nombre
    el stock es aleatorio
    """
    producto={} 

    producto["ID"]=idPro
    producto["Nombre"]=nombre
    stock=random.randint(300,500)
    producto["Stock"]=stock

    bodega.append(producto)

def quitar(idPro):
    """
    Quitar Productos
    --
    Funcion para quitar producto en base a un id

    """
    contador=0
    for i in bodega:

        if i["ID"]==idPro:
            bodega.pop(contador)

        contador+=1

def mostrarProducto():
    """
    Mostrar productos
    --
    Funcion para listar los productos de la bodega
    """
    for i in bodega:
        print("Producto: "+ str(i["Nombre"]) +" - Stock: " + str(i["Stock"]) )
        time.sleep(1) 

def verificarStock(idProd):
    """
    Verificar stock producto por id
    --
    funcion para buscar producto por id y verificar si tiene mas o menos de 400 unidades de stock
    """
    mensaje=""
    for i in bodega:
        if i["ID"]==idProd:
            if i["Stock"]<400:
                mensaje="Producto " +str(i["ID"]) + " tiene menos de 400 unidades"
            else:
                mensaje="Producto " +str(i["ID"]) + " tiene mas de 400 unidades"
    return mensaje


main()
sumar_Y_disminuirCantPro(1,100,1)
agregarProducto(4,"Platos")
quitar(4)
mostrarProducto()
print(verificarStock(1))


