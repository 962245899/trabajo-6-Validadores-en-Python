import os
#CALCULAR EL AREA DEL TRIANGULO
#DECLARARCION DE VARIABLES
area,base,altura=0.0,0.0,0.0

#INPUT
base=float(os.sys.argv[1])
altura=float(os.sys.argv[2])

# PROCESSING
area=(base*altura)/2

#VERIFICADOR
area_total1=(area>200)
area_total2=(150<=area<200)
area_total3=(50<=area<90)

# OUTPUT
print("##############################################")
print("# CALCULAR EL AREA DEL TRIANGULO")
print("##############################################")
print("#")
print("# base    :  ",                  base)
print("# altura  :  ",                altura)
print("# area total1   :  ",     area_total1)
print("# area total2   :  ",     area_total2)
print("# area total3    :  ",    area_total3)
print("##############################################")

#CONDICIONALES MULTIPLES:
if (area_total1):
    print("si el area es mayor que 200 es aceptable")
if (area_total2):
    print("si al area es menor que 200 no es aceptable")
if (area_total3):
    print("el area es mayor o igual 50 pero menor que 90 ")
#fin_if
