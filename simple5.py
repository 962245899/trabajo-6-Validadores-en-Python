import os
#DECLARARCION DE VARIABLES
costo_medio,costo_fijo_medio,costo_variable_medio=0.0,0.0,0.0

#INPUT
costo_fijo_medio=float(os.sys.argv[1])
costo_variable_medio=int(os.sys.argv[2])

# PROCESSING
costo_medio=(costo_fijo_medio+costo_variable_medio)

#VERIFICADOR
costo_medio_correcto=(costo_medio<900)

# OUTPUT
print("##########################################################")
print("# CALCULAR EL COSTO MEDIO")
print("##########################################################")
print("#")
print("# costo fijo medio      :  ",        costo_fijo_medio)
print("# costo variable medio  :  ",    costo_variable_medio)
print("# costo medio           :  ",             costo_medio)
print("##########################################################")

#CONDICIONAL SIMPLE:
if (costo_medio==True):
     print("el costo medio debe ser menor que 900")

 #fin_if
