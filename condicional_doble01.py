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
limite=(total>500)

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
print("el total es mayor que el limite?", limite)

#CONDICION SIMPLE
# si el monnto total hallada es mayor que 500 entonces lleve un kilo de arroz gratis
if (limite):
    print("GANASTE UN KILO DE ARROZ")
else:
    print("Gracias por su compra")
#fin_if
