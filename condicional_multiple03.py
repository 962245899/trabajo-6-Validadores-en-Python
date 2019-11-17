vendedor=os.sys.argv[2]
nº_de_mouse=float(os.sys.argv[3])
nº_de_laptop=float(os.sys.argv[4])
precio_unitario_mouse=float(os.sys.argv[5])
precio_unitario_laptop=float(os.sys.argv[6])

# PROCESSING
total = ((precio_unitario_mouse * nº_de_mouse)+(precio_unitario_laptop * nº_de_laptop))

#verificador
limite1=(total>3000)
limite2=(2500<=total<3000)
limite3=(0<total<2500)

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
print("el total es mayor que el limite?", limite1)
print("el total es mayor que el limite?", limite2)
print("el total es mayor que el limite?", limite3)

#CONDICIONAL DOBLE
#si la compra supera el limite entonces se lleva una tarjeta dorada
if (limite):
    print("GANASTE UNA TARJETA DORADA")
if (limite2):
    print("GANASTE UNA TARJETA PLATEADA")
if (limite3):
    print("GRACIAS POR SU COMPRA ")
#fin_if
