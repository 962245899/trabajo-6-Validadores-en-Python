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
energia_correcta1=(energia_mecanica<850)
energia_correcta2=(650<=energia_mecanica<850)
energia_correcta3=(100<=energia_mecanica<550)
# OUTPUT
print("##################################################")
print("# CALCULAR LA ENERGIA MECANICA")
print("##################################################")
print("#")
print("# energia potencial  :  ",  energia_potencial)
print("# energia cinetica   :  ",   energia_cinetica)
print("# energia mecanica   :  ",   energia_mecanica)
print("# energia correcta1  :  ",  energia_correcta1)
print("# energia correcta2  :  ",  energia_correcta2)
print("# energia correcta3  :  ",  energia_correcta3)
print("##################################################")

#CONDICONALES MULTIPLES:
if (energia_correcta1):
    print("si la energia es menor que 850 es aceptado")
if(energia_correcta2):
    print("si la energia es mayor que 850 no es aceptado")
if (energia_correcta3):
    ("si la energia es menor o igual que 100 pero menor que 550")
#fin_if
