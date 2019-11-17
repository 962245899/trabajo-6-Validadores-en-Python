import os
#INPUT
print("BOTICA SIEMPRE BIEN")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_jarabe=float(os.sys.argv[3])
nº_de_pastillas=float(os.sys.argv[4])
precio_unitario_jarabe=float(os.sys.argv[5])
precio_unitario_pastillas=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_jarabe * nº_de_jarabe)+(precio_unitario_pastillas * nº_de_pastillas))

#verificador
limite=(total>10)

# OUTPUT
print("#######################")
print("#BOTICA SIEMPRE BIEN#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_pastillas,"  nº_de_pastillas")
print("# Precio Unitario_pastillas  :  S/.", precio_unitario_pastillas)
print("# Item   :  ",nº_de_jarabe,"  nº_de_jarabe")
print("# Precio Unitario_jarabe   :  S/.", precio_unitario_jarabe)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es menor que el limite?", limite)

#CONDICION SIMPLE
#si la compra supera el limite entonces se lleva un vale
if (limite):
    print("GANASTE UN VALE PARA TU SIGUIENTE COMPRA")
#fin_if
