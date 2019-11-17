import os
#DECLARARCION DE VARIABLES
utilidad,ingreso_total,costo_total=0.0,0.0,0.0

#INPUT
ingreso_total=float(os.sys.argv[1])
costo_total=float(os.sys.argv[2])

# PROCESSING
utilidad=(ingreso_total-costo_total)

#VERIFICADOR
utilidad_correcto=(utilidad>250)

# OUTPUT
print("#############################################")
print("# CALCULAR EL LA UTILIDAD DE LA EMPRESA")
print("#############################################")
print("#")
print("# ingreso total  es :  ",     ingreso_total)
print("# costo total    es :  ",       costo_total)
print("# utilidad       es :  ",          utilidad)
print("#############################################")

#CONDICIONAL SIMPLE:
if (utilidad==True):
    print("la utilidad es mayor que 250")

#fin_if
