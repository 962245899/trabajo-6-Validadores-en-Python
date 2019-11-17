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
frecuencia_total1=(frecuencia>450)
frecuencia_total2=(250<=frecuencia<450)
frecuencia_total3=(35<=frecuencia<230)

# OUTPUT
print("##############################################")
print("# CALCULAR LA FRECUENCIA")
print("##############################################")
print("#")
print("# numero de vueltas  : ",  numero_de_vueltas)
print("# tiempo             : ",             tiempo)
print("# frecuencia         : ",         frecuencia)
print("# frecuencia total1 : ",  frecuencia_total1)
print("# frecuencia total2 : ",  frecuencia_total2)
print("# frecuencia total3 : ",  frecuencia_total3)
print("##############################################")

#CONDICONALES MULTIPLES:
if (frecuencia_total1):
    print("si la frecuenacia es mayo que 450 es aceptable")
if (frecuencia_total2):
    print("si la frecuencia es menor que 450 no es aceptable")
if (frecuencia_total3):
    print("si a frecuencia es menor o igual que 35 pero menor que 230")
#fin_if
