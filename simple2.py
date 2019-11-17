import os
#DECLARARCION DE VARIABLES
costo_total,costo_fijo,costo_variable=0.0,0.0,0.0

#INPUT
costo_fijo=float(os.sys.argv[1])
costo_variable=int(os.sys.argv[2])

# PROCESSING
costo_total=(costo_fijo+costo_variable)

#VERIFICADOR
costo_total_correcto=(costo_total>150)

# OUTPUT
print("#################################################")
print("# CALCULAR EL COSTO TOTAL")
print("#################################################")
print("#")
print("# costo fijo es     :  ",     costo_fijo)
print("# costo variable es :  ", costo_variable)
print("# costo total  es   :  ",    costo_total)
print("#################################################")

#CONDICIONAL SIMPLE:
if (costo_total==True):
    print("el costo total tiene que ser mayor que 150")

#fin_if

