import os
#INPUT
print("TOYOTA")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_autos=float(os.sys.argv[3])
nº_de_camionetas=float(os.sys.argv[4])
precio_unitario_autos=float(os.sys.argv[5])
precio_unitario_camionetas=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_camionetas* nº_de_camionetas)+(precio_unitario_autos * nº_de_autos))

#verificador
limite=(total>10000)

# OUTPUT
print("#######################")
print("#TOYOTA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_autos,"  nº_de_autos")
print("# Precio Unitario_autos  :  S/.", precio_unitario_autos)
print("# Item   :  ",nº_de_camionetas,"  nº_de_camionetas")
print("# Precio Unitario_camionetas   :  S/.", precio_unitario_camionetas)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se lleva una moto
if (limite):
    print("FELICIDADES GANASTE UNA MOTO")
else:
    print("Disfrute su compra")
#fin_if
