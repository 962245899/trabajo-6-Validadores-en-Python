import os
#DECLARARCION DE VARIABLES
aceleracion,velocidad_final,velocidaad_inicial,tiempo=0.0,0.0,0.0,0.0

#INPUT
velocidad_final=float(os.sys.argv[1])
velocidaad_inicial=float(os.sys.argv[2])
tiempo=int(os.sys.argv[3])

# PROCESSING
aceleracion=(velocidad_final-velocidaad_inicial)/tiempo

#VERIFICADOR
aceleracion_total=(aceleracion>50)

# OUTPUT
print("#######################################################")
print("# CALCULAR LA ACELERACION")
print("#######################################################")
print("#")
print("# velocidad final   :  m/s  ",     velocidad_final)
print("# velocidad inicial :  m/S  ",  velocidaad_inicial)
print("# tiempo            :   s   ",              tiempo)
print("# aceleracion       :  s^2  ",         aceleracion)
print("#######################################################")

#CONDICIONAL SIMPLE:
if (aceleracion==True):
    print("la aceleracion es mayor que 50")

#fin_if
