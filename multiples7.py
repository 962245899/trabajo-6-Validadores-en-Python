import os
#CALCULAR LA ENERGIA POTENCIAL GRAVITATORIA
#DECLARACION DE VARIABLES
energia_potencial_gravitatoria,masa,altura,gravedad=0.0,0.0,0.0,0.0

#INPUT
masa=float(os.sys.argv[1])
altura=int(os.sys.argv[2])
gravedad=float(os.sys.argv[3])

# PROCESSING
energia_potencial_gravitatoria=(masa*altura*gravedad)

#VERIFICADOR
energia_correcta1=(energia_potencial_gravitatoria<=3500)
energia_correcta2=(2500<=energia_potencial_gravitatoria<3500)
energia_correcta3=(1000<=energia_potencial_gravitatoria<2400)
# OUTPUT
print("#########################################################################")
print("# CALCULAR LA ENERGIA POTENCIAL GRAVITATORIA")
print("#########################################################################")
print("#")
print("# masa                           : ",                           masa)
print("# altura                         : ",                          altura)
print("# gravedad                       : ",                        gravedad)
print("# energia potencial gravitatoria : ",  energia_potencial_gravitatoria)
print("# energia correcta1 : ",                            energia_correcta1)
print("# energia correcta2 : ",                            energia_correcta2)
print("# energia correcta3 : ",                            energia_correcta3)
print("#########################################################################")

#CONDICONALES MULTIPLES:
if (energia_correcta1):
    print("si la energia es menor o igual que 3500 es admitible")
if (energia_correcta2):
    print("si la energia es mayor que 3500 no es admitible")
if (energia_correcta3):
    print("si la energia es menor o igual que 1000 pero menor que 2400")
#fin_if
