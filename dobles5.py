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
volumen_correcto=(volumen>=300)

# OUTPUT
print("##############################################")
print("# CALCULAR EL VOLUMEN DE LA PIRAMIDE")
print("##############################################")
print("#")
print("# AREA DE LA BASE  : ",  area_de_la_base)
print("# altura           : ",           altura)
print("# volumen          : ",          volumen)
print("##############################################")

#CONDICONALES DOBLES:
if (volumen_correcto==True):
    print("si el volumen es mayor o igaul que 300 es correcto")
else:
    print("si el volumen es menor que 300 no es correcto")
#fin_if
