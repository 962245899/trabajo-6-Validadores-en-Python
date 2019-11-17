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
area_total=(area>200)

# OUTPUT
print("##############################################")
print("# CALCULAR EL AREA DEL TRIANGULO")
print("##############################################")
print("#")
print("# base    :  ",    base)
print("# altura  :  ",  altura)
print("# area    :  ",    area)
print("##############################################")

#CONDICIONALES DOBLES:
if (area_total==True):
    print("si el area es mayor que 200 es aceptable")
else:
    print("si al area es menor que 200 no es aceptable")
#fin_if
