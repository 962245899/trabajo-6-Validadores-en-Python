import os
#INPUT
print("ALICORP")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_galletas=float(os.sys.argv[3])
nº_de_caramelos=float(os.sys.argv[4])
precio_unitario_galletas=float(os.sys.argv[5])
precio_unitario_caramelos=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_caramelos* nº_de_caramelos)+(precio_unitario_galletas * nº_de_galletas))

#verificador
limite1=(total>100)
limite2=(95<=total<100)
limite3=(0<total)

# OUTPUT
print("#######################")
print("#ALICORP#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_caramelos,"  nº_de_caramelos")
print("# Precio Unitario_caramelos  :  S/.", precio_unitario_caramelos)
print("# Item   :  ",nº_de_galletas,"  nº_de_galletas")
print("# Precio Unitario_galletas   :  S/.", precio_unitario_galletas)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite1)
print("el total es mayor que el limite?", limite2)
print("el total es mayor que el limite?", limite3)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se advierte que el consumo en exceso es dañino
if (limite1):
    print("EL CONSUMO EN EXCESO ES DAÑINO CUIDA TU SALUD ")
if (limite2):
    print("Disfrute el dulce de la vida")
if (limite3):
    print("GRACIAS POR SU COMPRA")
#fin_if
