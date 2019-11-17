import os
#DECLARARCION DE VARIABLES
area,base,altura,=0.0,0.0,0.0

#INPUT
base=float(os.sys.argv[1])
altura=int(os.sys.argv[2])

# PROCESSING
area=(base * altura)

#VERIFICADOR
area_correcto=(area<200)

# OUTPUT
print("############################################")
print("# CALCULAR EL AREA DEL RECTANGULO")
print("##########################")
print("#")
print("# area del rectangulo es  :     ",   area)
print("# Base es                :    ",    base)
print("# altura  es             :     ", altura)
print("############################################")
#CONDICIONAL SIMPLE:
if (area_correcto==True):
    print("el area tiene que ser menor que 200")
#fin_if
