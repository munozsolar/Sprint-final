
from typing import ClassVar


clientes=[]
def main():
    print("Sistema de clientes")
    clientes.append({"ID":1,"Nombre":"Juan","Apellido":"Perez","Edad":20,"Contraseña":11111})
    clientes.append({"ID":2,"Nombre":"Ramon","Apellido":"Cabrera","Edad":30,"Contraseña":22222})
    clientes.append({"ID":3,"Nombre":"Pedro","Apellido":"Pavez","Edad":25,"Contraseña":33333})
    clientes.append({"ID":4,"Nombre":"Diego","Apellido":"Perez","Edad":22,"Contraseña":444444})


def agregarclientes(id,nombre,apellido,edad,contrasena):
    """
    Agregar clientes
    --
    Funcion para agregar nuevos clientes
    """
    cliente={} 

    cliente["ID"]=id
    cliente["Nombre"]=nombre
    cliente["Apellido"]=apellido
    cliente["Edad"]=edad
    cliente["Contraseña"]=contrasena

    clientes.append(cliente)


def quitar(idCliente):
    """
    Quitar Clientes
    --
    Funcion para quitar cliente en base a un id

    """
    contador=0
    for i in clientes:

        if i["ID"]==idCliente:
            clientes.pop(contador)

        contador+=1 

def mostrarInfoCliente():
    """
    Mostrar info clientes
    --
    Funcion para imprimir por pantalla todos los clientes con su info.
    """
    for i in clientes:
        print("CLiente: "+ str(i["Nombre"]) + " " + str(i["Apellido"]) +" - Edad: " + str(i["Edad"]) +" - Password: " +str(i["Contraseña"]) )
        

main()
agregarclientes(5,"Ruben","Garcia",54,55555)
quitar(1)
mostrarInfoCliente()
