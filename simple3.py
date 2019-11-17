import os
#DECLARARCION DE VARIABLES
costo_fijo,costo_fijo_medio,produccion=0.0,0.0,0.0
#INPUT
costo_fijo=float(os.sys.argv[1])
produccion=int(os.sys.argv[2])

# PROCESSING
costo_fijo_medio=(costo_fijo/produccion)

#VERIFICADOR
costo_fijo_medio_correcto=(costo_fijo_medio>300)

# OUTPUT
print("#####################################################")
print("# CALCULAR EL COSTO FIJO MEDIO")
print("#####################################################")
print("#")
print("# costo fijo     es   :  ",        costo_fijo)
print("# produccion     es   :  ",        produccion)
print("# costo fijo medio es :  ",  costo_fijo_medio)
print("#####################################################")

#CONDICIONAL SIMPLE:
if (costo_fijo_medio==True):
    print("el costo fijo medio debe ser mayor que 300")
#fin_if


