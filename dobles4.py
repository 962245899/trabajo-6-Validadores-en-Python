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
fuerza_total=(fuerza<355)

# OUTPUT
print("##############################################")
print("# CALCULAR LA FUERZA")
print("##############################################")
print("#")
print("# masa          :  ",          masa)
print("# aceleracion   :  ",   aceleracion)
print("# fuerza        :  ",        fuerza)
print("##############################################")

#CONDICIONEALES DOBLES
if (fuerza_total==True):
  print("si la fuerza del bloque es menor que 355 es aceptable")
else:
    print("si la fuerza del bloque es mayor que 355 no es aceptable")
#fin_if
