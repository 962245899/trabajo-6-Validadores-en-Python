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
potencia_correcta1=(potencia_media<=750)
potencia_correcta2=(545<=potencia_media<750)
potencia_correcta3=(96<=potencia_media<500)
# OUTPUT
print("##############################################")
print("# CALCULAR LA POTENCIA MEDIA")
print("##############################################")
print("#")
print("# fuerza           :   ",             fuerza)
print("# velocidad media  :   ",    velocidad_media)
print("# potencia media   :   ",     potencia_media)
print("# potencia correcta1 : ", potencia_correcta1)
print("# potencia correcta2 : ", potencia_correcta2)
print("# potencia correcta3 : ", potencia_correcta3)
print("##############################################")

#CONDICONALES MULTIPLES:
if (potencia_correcta1):
    print("si la potencia es menor o igual que 750 es admitible")
if (potencia_correcta2):
    print("si la potencia es mayor que 750 no es admitible")
if (potencia_correcta3):
    print("si la potencia es menor o igua que 96 pero menor que 500")
#fin_if
