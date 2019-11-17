import os
#DECLARARCION DE VARIABLES
costo_variable_medio,costo_variable,produccion=0.0,0.0,0.0

#INPUT
costo_variable=float(os.sys.argv[1])
produccion=int(os.sys.argv[2])

# PROCESSING
costo_variable_medio=(costo_variable/produccion)

#VERIFICADOR
costo_variable_medio_correcto=(costo_variable_medio<800)

# OUTPUT
print("###########################################################")
print("# CALCULAR EL COSTO VARIABLE MEDIO")
print("###########################################################")
print("#")
print("# costo variable       es :   ",        costo_variable)
print("# produccion         es   :   ",            produccion)
print("# costo variable medio es :   ",  costo_variable_medio)
print("###########################################################")

#CONDICIONAL SIMPLE:
if (costo_variable_medio==True):
    print("el costo variable medio deber ser menos que 800")

#fin_if

