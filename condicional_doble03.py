import os
#DECLARACIÓN DE VARIABLES
cliente,vendedor,nº_de_laptop,nº_de_mouse,precio_unitario_laptop,precio_unitario_mouse="","",0,0,0.0,0.0

#INPUT
print("GLOBAL VISION")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_mouse=float(os.sys.argv[3])
nº_de_laptop=float(os.sys.argv[4])
precio_unitario_mouse=float(os.sys.argv[5])
precio_unitario_laptop=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_mouse * nº_de_mouse)+(precio_unitario_laptop * nº_de_laptop))

#verificador
limite=(total>3000)

# OUTPUT
print("#######################")
print("#GLOBAL VISION#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_mouse,"  nº_de_mouse")
print("# Precio Unitario_mouse   :  S/.", precio_unitario_mouse)
print("# Item   :  ",nº_de_laptop,"  nº_de_laptop")
print("# Precio Unitario_laptop   :  S/.", precio_unitario_laptop)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se lleva una tarjeta dorada
if (limite):
    print("GANASTE UNA TARJETA DORADA")
else:
    print("Regrese pronto")
#fin_if
