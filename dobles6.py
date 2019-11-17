import os
# CALCULAR EL AREA TOTAL DE LA PRIAMIDE
#DECLARACION DEVARIABLES
area_total,area_lateral,area_de_la_base=0.0,0.0,0.0

#INPUT
area_lateral=float(os.sys.argv[1])
area_de_la_base=int(os.sys.argv[2])

# PROCESSING
area_total=(area_lateral+area_de_la_base)

#VERIFICADOR
area_correcto=(area_total<=500)

# OUTPUT
print("##############################################")
print("# CALCULAR EL AREA TOTAL DE LA PRIAMIDE")
print("##############################################")
print("#")
print("# area lateral     :  ",      area_lateral)
print("# area de la base  :  ",   area_de_la_base)
print("# area total       :  ",        area_total)
print("##############################################")

#CONDICIONALES MULTIPLES:
if (area_correcto==True):
    print("si el area total es menor o igual que 300 es valido")
else:
    print("si el area total es mayor que 500 es invalido")
#fin_if
