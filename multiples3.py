import os
#CALCULAR LA FUERZA
#DECLARACION DE VARIABLES
fuerza,masa,aceleracion=0.0,0.0,0.0

#INPUT
masa=float(os.sys.argv[1])
aceleracion=int(os.sys.argv[2])

# PROCESSING
fuerza=(masa*aceleracion)

#VARIABLES
fuerza_total1=(fuerza<355)
fuerza_total2=(200<=fuerza<355)
fuerza_total3=(100<=fuerza<190)

# OUTPUT
print("##############################################")
print("# CALCULAR LA FUERZA")
print("##############################################")
print("#")
print("# masa          :  ",         masa)
print("# aceleracion   :  ",  aceleracion)
print("# fuerza        :  ",       fuerza)
print("# fuerza total1:  ", fuerza_total1)
print("# fuerza total2:  ", fuerza_total2)
print("# fuerza total3:  ", fuerza_total3)

print("##############################################")

#CONDICIONEALES MULTIPLES:
if (fuerza_total1):
  print("si la fuerza del bloque es menor que 355 es aceptable")
if (fuerza_total2):
    print("si la fuerza del bloque es mayor que 355 no es aceptable")
if (fuerza_total3):
    print("si la fuerza del bloque es menor o igual que 100 y menor que 190")
#fin_if

