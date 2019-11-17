import os
#INPUT
print("LA TABERNA")
cliente=os.sys.argv[1]
vendedor=os.sys.argv[2]
nº_de_vinos=float(os.sys.argv[3])
nº_de_pisco=float(os.sys.argv[4])
precio_unitario_vinos=float(os.sys.argv[3])
precio_unitario_pisco=float(os.sys.argv[5])

# PROCESSING
total = ((precio_unitario_pisco* nº_de_pisco)+(precio_unitario_vinos * nº_de_vinos))

#verificador
limite=(total>500)

# OUTPUT
print("#######################")
print("#LA TABERNA#")
print("# BOLETA DE VENTA")
print("#######################")
print("#")
print("# Cliente:  ", cliente)
print("# Item   :  ",nº_de_vinos,"  nº_de_vinos")
print("# Precio Unitario_vinos  :  S/.", precio_unitario_vinos)
print("# Item   :  ",nº_de_pisco,"  nº_de_pisco")
print("# Precio Unitario_pisco   :  S/.", precio_unitario_pisco)
print("# Total  :  S/.", total)
print("# nombre del vendedor:", vendedor)
print("#######################")
print("el total es mayor que el limite?", limite)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se lleva un sacacorchos
if (limite):
    print("GANASTE UN SACACORCHOS")
else:
    print("Tomar bebidas aloholicas en exceso es dañino")
#fin_if
