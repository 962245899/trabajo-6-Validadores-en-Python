import os
#INPUT
print("CLARO")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_celulares=float(os.sys.argv[3])
nº_de_accesorios=float(os.sys.argv[4])
precio_unitario_celulares=float(os.sys.argv[5])
precio_unitario_accesorios=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_celulares* nº_de_celulares)+(precio_unitario_accesorios * nº_de_accesorios))

#verificador
limite1=(total>1000)
limite2=(950<=total<1000)
limite3=(0<total<950)

# OUTPUT
print("#######################")
print("#CLARO#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_celulares,"  nº_de_celulares")
print("# Precio Unitario_celulares  :  S/.", precio_unitario_celulares)
print("# Item   :  ",nº_de_accesorios,"  nº_de_accesorios")
print("# Precio Unitario_accesorios   :  S/.", precio_unitario_accesorios)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite1)
print("el total es mayor que el limite?", limite2)
print("el total es mayor que el limite?", limite3)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se lleva un par de audifonos
if (limite):
    print("GANASTE UN PAR DE AUDIFONOS")
if (limite2):
    print("GANASTE UN PROTECTOR")
if (limite3):
    print("GRACIAS POR SU COMPRA")
#fin_if
