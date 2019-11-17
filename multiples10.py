import os
#CALCULAR LA VELOCIDAD FINAL
#DELARACION DE VARIABLES
velocidad_final,velocidad_inicial,aceleracion,tiempo=0.0,0.0,0.0,0.0

#INPUT
velocidad_inicial=float(os.sys.argv[1])
aceleracion=float(os.sys.argv[2])
tiempo=int(os.sys.argv[3])
# PROCESSING
velocidad_final=(velocidad_inicial+aceleracion*tiempo)

#VERIFICADOR
velocidad_final1=(velocidad_final>1000)
velocidad_final2=(665<=velocidad_final<1000)
velocidad_final3=(145<=velocidad_final<665)

# OUTPUT
print("###################################################")
print("# CALCULAR LA VELOCIDAD FINAL")
print("###################################################")
print("#")
print("# velocidad inicial  : ",   velocidad_inicial)
print("# aceleracion        : ",         aceleracion)
print("# tiempo             : ",              tiempo)
print("# velocidad final    : ",     velocidad_final)
print("# velocidad final1   : ",    velocidad_final1)
print("# velocidad final2   : ",    velocidad_final2)
print("# velocidad final3   : ",    velocidad_final3)
print("###################################################")

#CONDICONALES MULTIPLES:
if (velocidad_final1):
    print("si la velocidad es mayor que 1000 es aceptable")
if (velocidad_final2):
    print("si la velocidad es menor o igual que 665 pero menor que 1000")
if (velocidad_final3):
    print("si la velocidad es menor o igual que 145 pero menor que 665")
#fin_if
