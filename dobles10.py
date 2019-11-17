import os
#CALCULAR LA FRECUENCIA
# DECLARACION DE VARIABLES
frecuencia,numero_de_vueltas,tiempo=0.0,0.0,0.0

#INPUT
numero_de_vueltas=float(os.sys.argv[1])
tiempo=float(os.sys.argv[2])

# PROCESSING
frecuencia=(numero_de_vueltas/tiempo)

#VERIFICADOR
frecuencia_total=(frecuencia<=450)

# OUTPUT
print("##############################################")
print("# CALCULAR LA FRECUENCIA")
print("##############################################")
print("#")
print("# numero de vueltas  : ",  numero_de_vueltas)
print("# tiempo             : ",             tiempo)
print("# frecuencia         : ",         frecuencia)
print("##############################################")

#CONDICONALES DOBLES:
if (frecuencia_total==True):
    print("si la frecuenacia es menor o igual que 450 es aceptable")
else:
    print("si la frecuencia es mayor que 450 no es aceptable")
#fin_if
