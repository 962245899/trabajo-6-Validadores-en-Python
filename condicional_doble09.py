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
limite=(total>100)

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
print("el total es mayor que el limite?", limite)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se advierte que el consumo en exceso es dañino
if (limite):
    print("EL CONSUMO EN EXCESO ES DAÑINO CUIDA TU SALUD ")
else:
    print("Disfrute el dulce de la vida")
#fin_if
