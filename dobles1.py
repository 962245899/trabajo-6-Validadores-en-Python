import os
#BOLETA DE VENTA
#DECLARACION DE VARIABLES
cliente,produto,cantidad,monto_de_pago="","",0.0,0.0

#INPUT
cliente=(os.sys.argv[1])
produto=(os.sys.argv[2])
cantidad=int(os.sys.argv[3])
monto_de_pago=float(os.sys.argv[4])

#PROCESSING
total=(monto_de_pago*cantidad)

#VERIFICADOR
comprador_compulsivo=(total>500)

# OUTPUT
print("############################################")
print("# BOLETA DE VENTA")
print("############################################")
print("#")
print("# cliente  es    :       "  , cliente)
print("# producto es    :       " ,  produto)
print("# cantidad es    :        ", cantidad)
print("# monto de pago : ",    monto_de_pago)
print("# total               :     ",  total)
print("############################################")

#si el total es mayor que 500 entonces gana a tarjeta dorada:
if (comprador_compulsivo==True):
    print("GANASTE LA TARJETA DORADA")
else:
    print("GRACIAS POR SU COMPRA")
#fin_if
