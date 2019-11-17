import os
#DECLARARCION DE VARIABLES
presion,fuerza,area=0.0,0.0,0.0

#INPUT
fuerza=float(os.sys.argv[1])
area=int(os.sys.argv[2])

# PROCESSING
presion=(fuerza/area)

#VERIFICADOR
presion_total=(presion<140)

# OUTPUT
print("##############################################")
print("# CALCULAR LA PRESION")
print("##############################################")
print("#")
print("# fuerza   : ",   fuerza)
print("# area     : ",     area)
print("# presion  : ",  presion)
print("##############################################")
#CONDICIONAL SIMPLE:
if (presion==True):
    print("la presion deber ser menor que 140")

#fin_if
