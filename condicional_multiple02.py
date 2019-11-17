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
limite1=(total>50)
limite2=(40<=total<50)
limite3=(0<total<40)

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
print("el total es mayor que el limite?", limite1)
print("el total es mayor que el limite?", limite2)
print("el total es mayor que el limite?", limite3)

#CONDICIONAL MULTIPLE
#si la compra supera el limite entonces se lleva una tabla gratis
if (limite):
    print("GANASTE UNA TABLA ADICIONAL")
if (limite2):
    print("GANASTE UN DESCUENTO EN LA PROXIMA COMPRA")
if (limite3):
    print("GRACIAS POR SU COMPRA")
#fin_if

