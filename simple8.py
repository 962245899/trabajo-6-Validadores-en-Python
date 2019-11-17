import os
#DECLARARCION DE VARIABLES
distancia,velocidad,tiempo=0.0,0.0,0.0

#INPUT
velocidad=float(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

# PROCESSING
distancia=(velocidad*tiempo)

#VERIFICADOR
distancia_total=(distancia>100)

# OUTPUT
print("########################################")
print("# CALCULAR LA DISTANCIA")
print("########################################")
print("#")
print("# velocidad  : m/s   ",   velocidad)
print("# tiempo     : s     ",      tiempo)
print("# distancia  : m     ",   distancia)
print("########################################")
#CONDICIONAL SIMPLE:
if (distancia==True):
    print("la distancia es mayor que 100")

#fin_if
