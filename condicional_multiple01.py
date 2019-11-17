import os
#DECLARACION DE VARIABLES
cliente, vendedor,kg,precio_unitario,total="","",0.0,0.0,0.0
#input
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
kg=float(os.sys.argv[3])
precio_unitario=float(os.sys.argv[4])

# PROCESSING
total =round(precio_unitario * kg,)

#verificador
limite1=(total>500)
limite2=(450<=total<500)
limite3=(0<total<450)

# OUTPUT
print("#######################")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",kg,"  kg carne")
print("# Precio Unitario   :  S/.", precio_unitario)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite1)
print("el total es mayor que el limite?", limite2)
print("el total es mayor que el limite?", limite3)

#CONDICION SIMPLE
# si el monnto total hallada es mayor que 500 entonces lleve un kilo de arroz gratis
if (limite1):
    print("GANASTE UN KILO DE ARROZ")
#fin_if
if (limite2):
    print("GANASTE MEDIO KILO DE ARROZ")
#fin_if
if (limite3):
    print("Gracias por su compra")
#fin_if
