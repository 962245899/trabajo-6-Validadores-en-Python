import os
#INPUT
print("DONOFRIO")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_panetones=float(os.sys.argv[3])
nº_de_helados=float(os.sys.argv[4])
precio_unitario_panetones=float(os.sys.argv[5])
precio_unitario_helados=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_helados* nº_de_helados)+(precio_unitario_panetones * nº_de_panetones))

#verificador
limite=(total>100)
limite=(95<=total<100)
limite=(0<total<95)

# OUTPUT
print("#######################")
print("#DONOFRIO#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_panetones,"  nº_de_panetones")
print("# Precio Unitario_panetones  :  S/.", precio_unitario_panetones)
print("# Item   :  ",nº_de_helados,"  nº_de_helados")
print("# Precio Unitario_helados   :  S/.", precio_unitario_helados)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite1)
print("el total es menor que el limite?", limite2)
print("el total es menor que el limite?", limite3)

#CONDICION SIMPLE
#si la compra supera el limite entonces participa del sorteo de una cena navideña
if (limite1):
    print("FELICIDADES PATICIPAS DEL SORTEO DE UNA CENA NAVIDEÑA")
if (limite2):
    print("FELICIDADES GANASTE UN CUPON")
if (limite3):
    print("GRACIAS POR SU COMPRA")
#fin_if
