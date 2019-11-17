import os
#CALCULAR LA POTENCIA
#DECLARACION DE VARIABLES
potencia,trabajo,tiempo=0.0,0.0,0.0

#INPUT
trabajo=float(os.sys.argv[1])
tiempo=int(os.sys.argv[2])

# PROCESSING
potencia=(trabajo/tiempo)

#VERIFICADOR
potencia_total=(potencia>350)

# OUTPUT
print("##############################################")
print("# CALCULAR LA POTENCIA")
print("##############################################")
print("#")
print("# trabajo  :  ",    trabajo)
print("# tiempo   :  ",     tiempo)
print("# potencia :  ",   potencia)
print("##############################################")

#CONDICONALES DOBLES:
if (potencia_total==True):
    print("si la potencia es mayor que 350 es aceptable")
else:
    print("si la potencia es menor que 350 no es aceptable")
#fin_if
