import os
#DECLARACIÓN DE VARIABLES
cliente,vendedor,nº_de_tablas,precio_unitario,total="","",0,0.0,0.0

print("ASERRADERO TU BUENA TABLA")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_tablas=float(os.sys.argv[3])
precio_unitario=float(os.sys.argv[4])

# PROCESSING
total = round(precio_unitario * nº_de_tablas)

#verificador
limite=(total>50)

# OUTPUT
print("#######################")
print("#ASERRADERO TU BUENA TABLA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_tablas,"  nº_de_tablas")
print("# Precio Unitario   :  S/.", precio_unitario)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se lleva una tabla gratis
if (limite):
    print("GANASTE UNA TABLA ADICIONAL")
else:
    print("Sigue intentando")
#fin_if
