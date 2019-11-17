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
potencia_total1=(potencia>350)
potencia_total2=(100<=potencia<350)
potencia_total3=(50<=potencia<100)

# OUTPUT
print("##############################################")
print("# CALCULAR LA POTENCIA")
print("##############################################")
print("#")
print("# trabajo  :  ",    trabajo)
print("# tiempo   :  ",     tiempo)
print("# potencia :  ",   potencia)
print("# potencia total1:  ",potencia_total1)
print("# potencia total2 :  ",potencia_total2)
print("# potencia total3 :  ",potencia_total3)
print("##############################################")

#CONDICONALES MULTIPLES:
if (potencia_total1):
    print("si la potencia es mayor que 350 es aceptable")
if (potencia_total2):
    print("si la potencia es menor que 350 no es aceptable")
if (potencia_total3):
    print("si la potencia es menor o igual que 50 y menor que 90")
 #fin_if
