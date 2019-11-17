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
area1=(area_total>500)
area2=(400<=area_total<500)
area3=(100<=area_total<400)
# OUTPUT
print("##############################################")
print("# CALCULAR EL AREA TOTAL DE LA PRIAMIDE")
print("##############################################")
print("#")
print("# area lateral     :  ",    area_lateral)
print("# area de la base  :  ", area_de_la_base)
print("# area total       :  ",      area_total)
print("# area1       :        ",          area1)
print("# area2       :  ",                area2)
print("# area3      :  ",                 area3)
print("##############################################")

#CONDICIONALES MULTIPLES:
if (area1):
    print("si el area total es mayor o igual que 500 es valido")
if (area2):
    print("si el area total es menoor que 500 es invalido")
if (area3):
    print("si el area total es menor o igual que 100 pero menor que 400 ")
#fin_if
