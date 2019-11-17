import os
#DECLARARCION DE VARIABLES
costo_marginal,variacion_del_costo_total,variacion_de_la_produccion=0.0,0.0,0.0
#INPUT
variacion_del_costo_total=float(os.sys.argv[1])
variacion_de_la_produccion=float(os.sys.argv[2])

# PROCESSING
costo_marginal=(variacion_del_costo_total/variacion_de_la_produccion)

#VERIFICADOR
costo_marginal_correcto=(costo_marginal<450)

# OUTPUT
print("#####################################################################")
print("# CALCULAR EL COSTO MARGINAL")
print("#####################################################################")
print("#")
print("# variacion del costo total  :  ",    variacion_del_costo_total)
print("# variacion de la produccion :  ",   variacion_de_la_produccion)
print("# costo marginal             :  ",               costo_marginal)
print("#####################################################################")

#CONDICIONAL SIMPLE:
if (costo_marginal==True):
    print("el costo marginal deberia ser menor que 450")

#fin_if
