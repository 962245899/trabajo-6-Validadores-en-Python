import os
#INPUT
print("GRUPO GLORIA")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_leche=vendedor=os.sys.argv[2]
nº_de_frugos=float(os.sys.argv[4])
precio_unitario_leche=float(os.sys.argv[5])
precio_unitario_frugos=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_leche* nº_de_leche)+(precio_unitario_frugos * nº_de_frugos))

#verificador
limite1=(total>50)
limite2=(45<=total<50)
limite3=(0<total<45)

# OUTPUT
print("#######################")
print("#GRUPO GLORIA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_frugos,"  nº_de_frugos")
print("# Precio Unitario_frugos  :  S/.", precio_unitario_frugos)
print("# Item   :  ",nº_de_leche,"  nº_de_leche")
print("# Precio Unitario_leche   :  S/.", precio_unitario_leche)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite1)
print("el total es mayor que el limite?", limite2)
print("el total es mayor que el limite?", limite3)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se lleva un paneton
if (limite):
    print("GANASTE UN PANETON")
if (limite2):
    print("GANASTE UN VALE")
if(limite3):
    print("GRACIAS POR SU COMPRA")
#fin_if
