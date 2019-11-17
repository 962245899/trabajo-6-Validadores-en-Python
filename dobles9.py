import os
#CALCULAR LA POTENCIA MEDIA
# DECLARACION DE VARIABLES
potencia_media,fuerza,velocidad_media=0.0,0.0,0.0

#INPUT
fuerza=float(os.sys.argv[1])
velocidad_media=float(os.sys.argv[2])

# PROCESSING
potencia_media=(fuerza*velocidad_media)

#VERIFICADOR
potencia_correcta=(potencia_media<=750)

# OUTPUT
print("##############################################")
print("# CALCULAR LA POTENCIA MEDIA")
print("##############################################")
print("#")
print("# fuerza           : ",            fuerza)
print("# velocidad media  : ",   velocidad_media)
print("# potencia media   : ",    potencia_media)
print("##############################################")

#CONDICONALES DOBLES:
if (potencia_correcta==True):
    print("si la potencia es menor o igual que 750 es admitible")
else:
    print("si la potencia es mayor que 750 no es admitible")
#fin_if
