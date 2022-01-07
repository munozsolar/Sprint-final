bodega_a=0
bodega_b=600

def consultarTipoEnvio(opc):
    """
    Consultar tipo envio
    --
    Funcion para validar si el envio es largo o rapido
    """
    if opc=="Rapido":
        distancia=int(input("Ingresar km, tiene que ser menor o igual a 1000 km: "))
        if distancia>1000:
            print("KM ingresado no valido")
        else:
            global bodega_a
            if bodega_a<=500:
                bodega_a+=10
        
    elif opc=="Largo":
        distancia=int(input("Ingresar km, tiene que ser mayor a 1000 km: "))
        if distancia<=1000:
            print("KM ingresado no valido")
        else:
            global bodega_b
            if bodega_b<=500:
                bodega_b+=50

consultarTipoEnvio("Largo")
print("Bodega a =",bodega_a," - Bodega b =", bodega_b)