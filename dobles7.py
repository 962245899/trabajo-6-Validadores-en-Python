import os
#CALCULAR LA ENERGIA MECANICA
#DECLARACION DE VARIABLES
energia_mecanica,energia_potencial,energia_cinetica=0.0,0.0,0.0

#INPUT
energia_potencial=float(os.sys.argv[1])
energia_cinetica=int(os.sys.argv[2])

# PROCESSING
energia_mecanica=(energia_cinetica+energia_potencial)

#VERIFICADOR
energia_correcta=(energia_mecanica<850)

# OUTPUT
print("##################################################")
print("# CALCULAR LA ENERGIA MECANICA")
print("##################################################")
print("#")
print("# energia potencial  :  ",  energia_potencial)
print("# energia cinetica   :  ",   energia_cinetica)
print("# energia mecanica   :  ",   energia_mecanica)
print("##################################################")

#CONDICONALES DOBLES:
if (energia_correcta==True):
    print("si la energia es menor que 850 es aceptado")
else:
    print("si la energia es mayor que 850 no es aceptado")
#fin_if
