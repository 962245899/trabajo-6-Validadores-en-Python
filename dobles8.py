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
energia_correcta=(energia_potencial_gravitatoria<=3500)
# OUTPUT
print("#########################################################################")
print("# CALCULAR LA ENERGIA POTENCIAL GRAVITATORIA")
print("#########################################################################")
print("#")
print("# masa                           : ",                           masa)
print("# altura                         : ",                          altura)
print("# gravedad                       : ",                        gravedad)
print("# energia potencial gravitatoria : ",  energia_potencial_gravitatoria)
print("#########################################################################")

#CONDICONALES DOBLES:
if (energia_correcta==True):
    print("si la energia es menor o igual que 3500 es admitible")
else:
    print("si la energia es mayor que 3500 no es admitible")
#fin_if
