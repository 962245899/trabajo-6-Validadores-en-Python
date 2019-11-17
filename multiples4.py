import os
# CALCULAR EL VOLUMEN DE LA PIRAMIDE
#DECLARACION DE VARIABLES
volumen,area_de_la_base,altura=0.0,0.0,0.0

#INPUT
area_de_la_base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

# PROCESSING
volumen=(area_de_la_base*altura)/3

#VERIFICADOR
volumen1=(volumen>=300)
volumen2=(250<=volumen<300)
volumen3=(50<=volumen<240)
# OUTPUT
print("##############################################")
print("# CALCULAR EL VOLUMEN DE LA PIRAMIDE")
print("##############################################")
print("#")
print("# AREA DE LA BASE  : ",  area_de_la_base)
print("# altura           : ",           altura)
print("# volumen          : ",          volumen)
print("##############################################")

#CONDICONALES MULTIPLES:
if (volumen1):
    print("si el volumen es mayor o igaul que 300 es correcto")
if (volumen2):
    print("si el volumen es menor que 300 no es correcto")
if (volumen3) :
    print("si el volumen es menor o igual que 50 pero menor que 240")
#fin_if
